from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router as email_router
from app.config import settings, limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI(title="Serviço de formulário de contato")

# conecta o Limiter ao app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
