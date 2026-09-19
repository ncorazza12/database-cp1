from pydantic import BaseModel, EmailStr, Field, field_validator


class AlunoCreate(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome do aluno")
    email: EmailStr
    idade: int = Field(..., ge=16, description="Idade mínima de 16 anos")
    curso: str = Field(..., min_length=1, description="Curso do aluno")

    @field_validator("nome", "curso")
    @classmethod
    def nao_pode_ser_vazio(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Este campo não pode ser vazio")
        return v


class AlunoUpdate(AlunoCreate):
    pass


class AlunoResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    idade: int
    curso: str
