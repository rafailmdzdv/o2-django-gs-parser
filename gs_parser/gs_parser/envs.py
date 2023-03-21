from pathlib import Path

from pydantic.env_settings import BaseSettings


class Env(BaseSettings):

    SECRET_KEY: str
    POSTGRE_DSN: str

    class Config:
        env_file = f'{Path(__file__).resolve().parent.parent.parent}/.env'


env = Env()
