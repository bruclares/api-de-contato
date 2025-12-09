import os
from pydantic_settings import BaseSettings
from fastapi_mail import ConnectionConfig

class Settings(BaseSettings):
  MAIL_USERNAME: str
  MAIL_PASSWORD: str
  MAIL_FROM: str
  MAIL_PORT: str
  MAIL_SERVER: str
  MAIL_TO: str

  # configuração do fastapi-mail centralizada
  @property
  def email_conf(self):
    return ConnectionConfig(
      MAIL_USERNAME=self.MAIL_USERNAME,
      MAIL_PASSWORD=self.MAIL_PASSWORD,
      MAIL_FROM=self.MAIL_FROM,
      MAIL_PORT=self.MAIL_PORT,
      MAIL_SERVER=self.MAIL_SERVER,
      MAIL_STARTTLS=True,
      MAIL_SSL_TLS=False,
      USE_CREDENTIALS=True,
      VALIDATE_CERTS=True
    )

  class Config:
    env_file = ".env"

# instância única para usar no app todo
settings = Settings()
