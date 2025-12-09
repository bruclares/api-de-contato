from pydantic import BaseModel, EmailStr


class ContatoSchema(BaseModel):
    nome: str
    email: EmailStr
    mensagem: str
