# API de Gerenciamento de Produtos
![GitHub repo size](https://img.shields.io/github/repo-size/joseamaury/API-python)
![GitHub last commit](https://img.shields.io/github/last-commit/joseamaury/API-python)
![GitHub issues](https://img.shields.io/github/issues/joseamaury/API-python)
![GitHub stars](https://img.shields.io/github/stars/joseamaury/API-python?style=social)
![Python Versions](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/github/license/joseamaury/API-python)

---

## Descrição Geral

Esta API foi desenvolvida em **Python** usando **FastAPI**, com o objetivo de gerenciar produtos de forma simples. Permite criar, listar, atualizar e deletar produtos, simulando um sistema básico de estoque ou loja online.  
Este projeto faz parte de um desafio pessoal de aprendizado em Python, inspirado em um curso em JavaScript, mas implementando a solução em Python para praticar boas práticas de desenvolvimento de APIs.

---

## Objetivos

- Criar uma API RESTful com Python e FastAPI  
- Implementar operações CRUD (Create, Read, Update, Delete) para produtos  
- Praticar envio de requisições e manipulação de dados via JSON  
- Documentar a API para uso e versionamento no GitHub  

---

## Funcionalidades

| Endpoint                | Método | Descrição                      |
|------------------------|--------|-------------------------------|
| `/produtos`            | GET    | Lista todos os produtos cadastrados |
| `/produtos`            | POST   | Adiciona um novo produto       |
| `/produtos/{produto_id}` | PUT    | Atualiza um produto existente  |
| `/produtos/{produto_id}` | DELETE | Remove um produto específico   |

---

## Tecnologias Utilizadas

- **Python 3.x** – Linguagem principal  
- **FastAPI** – Framework para APIs rápidas e eficientes  
- **Pydantic** – Validação e modelagem de dados  
- **Uvicorn** – Servidor ASGI para rodar a aplicação  
- **Insomnia / Postman** – Teste de requisições HTTP  

---

## Estrutura de Dados

### Produto

| Campo     | Tipo   | Obrigatório | Descrição                          |
|-----------|--------|-------------|----------------------------------|
| id        | int    | Sim         | Identificador único do produto    |
| nome      | str    | Sim         | Nome do produto (2-50 caracteres)|
| preco     | float  | Sim         | Preço do produto (maior que 0)   |
| descricao | str    | Não         | Descrição opcional (até 200 caracteres) |

### ProdutoCreate (para criação)

| Campo     | Tipo   | Obrigatório | Descrição                |
|-----------|--------|-------------|-------------------------|
| nome      | str    | Sim         | Nome do produto          |
| preco     | float  | Sim         | Preço do produto         |
| descricao | str    | Não         | Descrição opcional       |

### ProdutoUpdate (para atualização)

| Campo     | Tipo   | Obrigatório | Descrição            |
|-----------|--------|-------------|---------------------|
| nome      | str    | Não         | Novo nome do produto  |
| preco     | float  | Não         | Novo preço do produto |
| descricao | str    | Não         | Nova descrição        |

---

## Exemplos de Requisições e Respostas

### 1. Listar produtos

**GET /produtos**

**Resposta:**

[
{

"id": 1,
"nome": "Mouse Gamer",
"preco": 199.90,
"descricao": "Mouse RGB 16000 DPI"

},
{

"id": 2,
"nome": "Teclado Mecânico",
"preco": 299.90,
"descricao": "Teclado RGB com switches azuis"

}
]


### 2. Criar produto

**POST /produtos**

**Corpo da requisição:**

{

"nome": "Headset Gamer",
"preco": 149.90,
"descricao": "Headset com microfone retrátil"

}


**Resposta:**

{

"id": 3,
"nome": "Headset Gamer",
"preco": 149.90,
"descricao": "Headset com microfone retrátil"

}



### 3. Atualizar produto

**PUT /produtos/3**

**Corpo da requisição:**

{

"preco": 159.90

}



**Resposta:**

{

"id": 3,
"nome": "Headset Gamer",
"preco": 159.90,
"descricao": "Headset com microfone retrátil"

}


### 4. Deletar produto

**DELETE /produtos/3**

**Resposta:**

{

"message": "Produto removido com sucesso",
"produto": {
"id": 3,
"nome": "Headset Gamer",
"preco": 159.90,
"descricao": "Headset com microfone retrátil"
}

}


---

## Instruções de Instalação

**1. Clonar o repositório**

git clone https://github.com/joseamaury/API-python.git
cd API-python



**2. Criar e ativar o ambiente virtual**

Windows
python -m venv venv
venv\Scripts\activate

Linux / Mac
python -m venv venv
source venv/bin/activate



**3. Instalar dependências**

pip install -r requirements.txt



**4. Executar a API**

uvicorn main:app --reload



**5. Abrir documentação interativa**

Acesse no navegador:

http://127.0.0.1:8000/docs



---

## Observações

Esta API utiliza armazenamento em memória, então os produtos somem ao reiniciar o servidor.  
Para persistência, é recomendável salvar os produtos em arquivo JSON ou usar um banco de dados.  
Projeto desenvolvido como desafio de aprendizado em Python, inspirado em um curso de JavaScript.

---

## Contribuições

Pull requests são bem-vindos!  
Para melhorias, abra uma issue ou envie uma sugestão.
