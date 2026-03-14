# 📚 Biblioteca API

API REST desenvolvida em **Python com Flask** para gerenciamento de livros em uma biblioteca.
Este projeto foi criado com o objetivo de praticar conceitos fundamentais de **desenvolvimento backend**, incluindo criação de APIs REST, manipulação de banco de dados e versionamento com Git.

---

## 🚀 Tecnologias Utilizadas

* **Python**
* **Flask**
* **SQLite**
* **Git / GitHub**
* **Thunder Client** (testes de API)

---

## 📂 Estrutura do Projeto

```
biblioteca_api
│
├── app.py            # Arquivo principal da API
├── requirements.txt  # Dependências do projeto
├── .gitignore        # Arquivos ignorados pelo Git
└── database.db       # Banco de dados SQLite
```

---

## ⚙️ Instalação

Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/biblioteca_api.git
```

Acesse a pasta do projeto:

```
cd biblioteca_api
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

## ▶️ Executando a Aplicação

Para iniciar a API, execute:

```
python app.py
```

O servidor será iniciado em:

```
http://127.0.0.1:5000
```

---

## 📌 Endpoints da API

### 📚 Listar todos os livros

```
GET /livros
```

Retorna uma lista com todos os livros cadastrados.

---

### ➕ Adicionar um livro

```
POST /livros
```

Exemplo de requisição JSON:

```
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899
}
```

---

### 🔎 Buscar livro por ID

```
GET /livros/{id}
```

Exemplo:

```
GET /livros/1
```

---

### ✏️ Atualizar um livro

```
PUT /livros/{id}
```

Exemplo de JSON:

```
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1900
}
```

---

### ❌ Remover um livro

```
DELETE /livros/{id}
```

---

## 🧪 Testando a API

A API pode ser testada utilizando ferramentas como:

* Thunder Client (VS Code)
* Postman
* Insomnia

---

## 📚 Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

* criação de **APIs REST**
* uso do **framework Flask**
* operações **CRUD**
* integração com **SQLite**
* versionamento com **Git e GitHub**

---

## 👨‍💻 Autor

Desenvolvido por **Rafael Paiva**
Estudante de **Análise e Desenvolvimento de Sistemas**.

