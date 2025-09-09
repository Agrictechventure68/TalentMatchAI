import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "TalentMatchAI"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./talentmatchai.db"

    class Config:
        env_file = ".env"

settings = Settings()