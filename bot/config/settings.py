from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    TOKEN: str
    BACKEND_URL: str


settings = Settings()
