import resend
from fastapi import BackgroundTasks
from app.config import settings
from app.schemas import ContatoSchema
from app.logger import log

resend.api_key = settings.RESEND_API_KEY


class EmailService:
    async def _send_email_wrapper(self, contato: ContatoSchema):
        """
        Envia o e-mail usando a API do Resend.
        """
        try:
            log.info(f"Iniciando envio de e-mail via Resend para: {settings.MAIL_TO}")
            html_content = f"""
            <h3>Novo contato recebido pelo site!</h3>
            <p><strong>Nome:</strong> {contato.nome}</p>
            <p><strong>E-mail do Cliente:</strong> {contato.email}</p>
            <p><strong>Mensagem:</strong><br>{contato.mensagem}</p>
            """

            # envia via API
            params = {
                "from": "DCTec Site <onboarding@resend.dev>",
                "to": [settings.MAIL_TO],
                "subject": f"Novo Contato: {contato.nome}",
                "html": html_content,
                "reply_to": contato.email,  # Permite responder direto pro cliente
            }

            r = resend.Emails.send(params)
            log.success(f"E-mail enviado com sucesso! ID do Resend: {r.get('id')}")

        except Exception as e:
            log.error(f"FALHA ao enviar pelo Resend: {str(e)}")

    async def enviar_contato(
        self, contato: ContatoSchema, background_tasks: BackgroundTasks
    ):
        """
        Apenas delega a tarefa para background.
        """
        # Agenda o envio para não travar a resposta do usuário
        background_tasks.add_task(self._send_email_wrapper, contato)
