from fastapi import APIRouter, BackgroundTasks, Request
from app.schemas import ContatoSchema
from app.services import EmailService
from app.config import limiter

# cria um agrupador de rotas
router = APIRouter()

# instancia o serviço
service = EmailService()


@router.post("/send")
@limiter.limit("5/minute")
async def send_email(
    request: Request, contato: ContatoSchema, background_tasks: BackgroundTasks
):
    # recebe e valida
    # chama o serviço
    await service.enviar_contato(contato, background_tasks)

    # retorna a resposta
    return {"message": "Mensagem enviada com sucesso", "status": "ok"}
