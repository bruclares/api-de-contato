from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from app.config import settings
from app.schemas import ContatoSchema
from app.logger import log


class EmailService:
    async def _send_email_wrapper(self, message: MessageSchema):
        """
        Método interno que executa o envio real com tratamento de erro e logs.
        """
        fm = FastMail(settings.email_conf)

        try:
            log.info(f"Iniciando envio de e-mail para: {settings.MAIL_TO}")
            await fm.send_message(message)
            log.success(f"E-mail enviado com sucesso para {settings.MAIL_TO}")

        except Exception as e:
            log.error(f"FALHA CRÍTICA ao enviar e-mail. Erro: {str(e)}")

    async def enviar_contato(
        self, contato: ContatoSchema, background_tasks: BackgroundTasks
    ):
        """
        Prepara a mensagem e delega para o background.
        """
        message = MessageSchema(
            subject=f"Novo contato do site: {contato.nome}",
            recipients=[settings.MAIL_TO],
            body=f"""
      <h3>Nova mensagem recebida!</h3>
      <p><strong>Nome:</strong> {contato.nome}</p>
      <p><strong>E-mail:</strong> {contato.email}</p>
      <p><strong>Mensagem:</strong><br>{contato.mensagem}</p>
      """,
            subtype=MessageType.html,
        )

        fm = FastMail(settings.email_conf)

        # agenda o envio (não trava a requisição)
        background_tasks.add_task(self._send_email_wrapper, message)
