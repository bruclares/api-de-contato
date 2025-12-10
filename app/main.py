import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.routers import router as email_router
from app.config import settings, limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from app.logger import log

app = FastAPI(title="Serviço de formulário de contato")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    detalhes_erro = []
    for error in exc.errors():
        # Pega o campo e a mensagem de erro de forma limpa
        campo = error.get("loc")[-1]
        msg = error.get("msg")
        detalhes_erro.append(f"{campo}: {msg}")

    log.warning(f"Dados inválidos recebidos: {detalhes_erro}")

    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    log_status = f"{response.status_code}"
    if response.status_code < 400:
        log_method = log.info
    else:
        log_method = log.warning

    log_method(
        f"Path: {request.method} {request.url.path} | "
        f"Status: {log_status} | "
        f"Tempo: {process_time:.4f}s"
    )
    return response


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
    log.info("Health check realizado")
    return {"message": "API de Contato está online! 🚀"}


# inclui as rotas
app.include_router(email_router, prefix="/api")

# Para rodar: uvicorn app.main:app --reload
