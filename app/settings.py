from pydantic import BaseSettings, Field
import os
from dotenv import load_dotenv

# Ensure environment variables are loaded
load_dotenv()

class Settings(BaseSettings):
    postgres_user: str = Field(os.environ.get('POSTGRES_USER', 'test_user'))
    postgres_password: str = Field(os.environ.get('POSTGRES_PASSWORD', 'test_password'))
    postgres_db: str = Field(os.environ.get('POSTGRES_DB', 'test_db'))
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
