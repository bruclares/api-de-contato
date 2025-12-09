from pydantic import BaseModel, EmailStr, Field, field_validator


class ContatoSchema(BaseModel):
    nome: str = Field(
        ..., min_length=2, max_length=100, description="Nome completo do remetente"
    )
    email: EmailStr = Field(..., description="E-mail válido para contato")
    mensagem: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        description="Conteúdo da mensagem (máx 2000 caracteres)",
    )

    @field_validator("nome", "mensagem")
    def remove_espacos(cls, v):
        if v:
            return v.strip()
        return v
