from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router as email_router
from app.config import settings

app = FastAPI(title="Serviço de formulário de contato")

# configuração de cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "API de Contato está online! 🚀"}


# inclui as rotas
app.include_router(email_router, prefix="/api")

# Para rodar: uvicorn app.main:app --reload
