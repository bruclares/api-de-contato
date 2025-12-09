from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from app.config import settings
from app.schemas import ContatoSchema


class EmailService:
    async def enviar_contato(
        self, contato: ContatoSchema, background_tasks: BackgroundTasks
    ):
        """
        Prepara e agenda o envio do e-mail em background.
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
        background_tasks.add_task(fm.send_message, message)
