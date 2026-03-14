from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect("database.db")

# Criar tabela se não existir
with conectar() as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano INTEGER
    )
    """)

# Listar livros
@app.route("/livros", methods=["GET"])
def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    lista = []
    for livro in livros:
        lista.append({
            "id": livro[0],
            "titulo": livro[1],
            "autor": livro[2],
            "ano": livro[3]
        })

    return jsonify(lista)


# Adicionar livro
@app.route("/livros", methods=["POST"])
def adicionar_livro():
    dados = request.json

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        (dados["titulo"], dados["autor"], dados["ano"])
    )
    conn.commit()

    return jsonify({"mensagem": "Livro adicionado com sucesso"})


# Buscar livro por ID
@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE id=?", (id,))
    livro = cursor.fetchone()

    if livro:
        return jsonify({
            "id": livro[0],
            "titulo": livro[1],
            "autor": livro[2],
            "ano": livro[3]
        })

    return jsonify({"erro": "Livro não encontrado"})


# Atualizar livro
@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.json

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE livros SET titulo=?, autor=?, ano=? WHERE id=?",
        (dados["titulo"], dados["autor"], dados["ano"], id)
    )
    conn.commit()

    return jsonify({"mensagem": "Livro atualizado"})


# Deletar livro
@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id=?", (id,))
    conn.commit()

    return jsonify({"mensagem": "Livro deletado"})


if __name__ == "__main__":
    app.run(debug=True)
