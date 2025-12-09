from fastapi import FastAPI
from fastapi.middleware.cors import CORS 
from app.routers import router as email_router

app = FastAPI(title="Serviço de formulário de contato")

# configuração de cors
app.add_middleware(
  CORS,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

# inclui as rotas
app.include_router(email_router, prefix='/api')

# Para rodar: uvicorn app.main:app --reload