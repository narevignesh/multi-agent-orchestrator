from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str
    api_url: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()