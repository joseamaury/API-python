from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# Criando a aplicação FastAPI
app = FastAPI(title="API de Produtos", description="Gerenciamento simples de produtos", version="1.0")

# ================================
# MODELO DE DADOS
# ================================
class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    descricao: Optional[str] = None

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=50, description="Nome do produto (2-50 caracteres)")
    preco: float = Field(..., gt=0, description="Preço deve ser maior que 0")
    descricao: Optional[str] = Field(None, max_length=200, description="Descrição opcional (até 200 caracteres)")

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=50)
    preco: Optional[float] = Field(None, gt=0)
    descricao: Optional[str] = Field(None, max_length=200)

# Banco de dados em memória (simples)
produtos: List[Produto] = []
id_counter = 1

# ================================
# ENDPOINTS
# ================================

# Listar todos os produtos
@app.get("/produtos", response_model=List[Produto])
def listar_produtos():
    return produtos

# Criar novo produto
@app.post("/produtos", response_model=Produto, status_code=201)
def criar_produto(produto: ProdutoCreate):
    global id_counter

    novo_produto = Produto(
        id=id_counter,
        nome=produto.nome,
        preco=produto.preco,
        descricao=produto.descricao
    )
    produtos.append(novo_produto)
    id_counter += 1

    return novo_produto

# Atualizar produto existente
@app.put("/produtos/{produto_id}", response_model=Produto)
def atualizar_produto(produto_id: int, produto: ProdutoUpdate):
    for p in produtos:
        if p.id == produto_id:
            if produto.nome is not None:
                p.nome = produto.nome
            if produto.preco is not None:
                p.preco = produto.preco
            if produto.descricao is not None:
                p.descricao = produto.descricao
            return p

    raise HTTPException(status_code=404, detail="Produto não encontrado")

# Deletar produto
@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    for p in produtos:
        if p.id == produto_id:
            produtos.remove(p)
            return {"message": "Produto removido com sucesso", "produto": p}

    raise HTTPException(status_code=404, detail="Produto não encontrado")
