from fastapi import FastAPI, HTTPException, status
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.errors import DuplicateKeyError

from database import alunos_collection
from models import AlunoCreate, AlunoUpdate, AlunoResponse

app = FastAPI(title="API de Gerenciamento de Alunos")


def aluno_helper(aluno) -> dict:
    """Converte o documento do MongoDB para o formato de resposta da API."""
    return {
        "id": str(aluno["_id"]),
        "nome": aluno["nome"],
        "email": aluno["email"],
        "idade": aluno["idade"],
        "curso": aluno["curso"],
    }


@app.post("/alunos", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno: AlunoCreate):
    try:
        resultado = alunos_collection.insert_one(aluno.model_dump())
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um aluno cadastrado com este e-mail."
        )
    novo_aluno = alunos_collection.find_one({"_id": resultado.inserted_id})
    return aluno_helper(novo_aluno)


@app.get("/alunos", response_model=list[AlunoResponse])
def listar_alunos():
    alunos = list(alunos_collection.find())
    return [aluno_helper(a) for a in alunos]


@app.get("/alunos/{aluno_id}", response_model=AlunoResponse)
def consultar_aluno(aluno_id: str):
    try:
        oid = ObjectId(aluno_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")

    aluno = alunos_collection.find_one({"_id": oid})
    if not aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")
    return aluno_helper(aluno)


@app.put("/alunos/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(aluno_id: str, aluno: AlunoUpdate):
    try:
        oid = ObjectId(aluno_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")

    existente = alunos_collection.find_one({"_id": oid})
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")

    # Verifica se o novo e-mail já pertence a outro aluno
    duplicado = alunos_collection.find_one({"email": aluno.email, "_id": {"$ne": oid}})
    if duplicado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe outro aluno cadastrado com este e-mail."
        )

    alunos_collection.update_one({"_id": oid}, {"$set": aluno.model_dump()})
    atualizado = alunos_collection.find_one({"_id": oid})
    return aluno_helper(atualizado)


@app.delete("/alunos/{aluno_id}", status_code=status.HTTP_200_OK)
def excluir_aluno(aluno_id: str):
    try:
        oid = ObjectId(aluno_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")

    resultado = alunos_collection.delete_one({"_id": oid})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")

    return {"mensagem": "Aluno removido com sucesso."}
