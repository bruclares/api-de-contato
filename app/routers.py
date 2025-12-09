from fastapi import APIRouter, BackgroundTasks
from app.schemas import ContatoSchema
from app.services import EmailService

# cria um agrupador de rotas
router = APIRouter()

# instancia o serviço 
service = EmailService

@router.post("/send")
async def send_email(contato: ContatoSchema, background_tasks: BackgroundTasks):
  # recebe e valida
  # chama o serviço
  await service.enviar_contato(contato, background_tasks)

  # retorna a resposta
  return {"message": "Mensagem enviada com sucesso", "status": "ok"}