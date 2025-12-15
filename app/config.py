import os
from typing import List
from pydantic_settings import BaseSettings
from slowapi import Limiter
from slowapi.util import get_remote_address


class Settings(BaseSettings):
    RESEND_API_KEY: str
    MAIL_TO: str
    ALLOWED_ORIGINS: str = "*"

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"


# instância única para usar no app todo
settings = Settings()

limiter = Limiter(key_func=get_remote_address)
