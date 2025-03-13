from pydantic import BaseSettings, Field
import os
from dotenv import load_dotenv

# Ensure environment variables are loaded
load_dotenv()

class Settings(BaseSettings):
    postgres_user: str = Field(os.environ.get('POSTGRES_USER', 'paracas'))
    postgres_password: str = Field(os.environ.get('POSTGRES_PASSWORD', 'paracas2024'))
    postgres_db: str = Field(os.environ.get('POSTGRES_DB', 'payment_service'))
    postgres_host: str = Field(os.environ.get('POSTGRES_HOST', 'db'))
    postgres_port: str = Field(os.environ.get('POSTGRES_PORT', '5432'))

    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
