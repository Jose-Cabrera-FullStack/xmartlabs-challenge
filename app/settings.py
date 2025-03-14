from pydantic import BaseSettings, Field
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # postgres settings
    postgres_user: str = Field(os.environ.get('POSTGRES_USER', 'app'))
    postgres_password: str = Field(os.environ.get('POSTGRES_PASSWORD', 'app2024'))
    postgres_db: str = Field(os.environ.get('POSTGRES_DB', 'app_service'))
    postgres_host: str = Field(os.environ.get('POSTGRES_HOST', 'db'))
    postgres_port: str = Field(os.environ.get('POSTGRES_PORT', '5432'))

    # aws bucket settings
    aws_access_key_id: str = Field(os.environ.get("AWS_ACCESS_KEY_ID", "your-access"))
    aws_secret_access_key: str = Field(os.environ.get("AWS_SECRET_ACCESS_KEY", "your-secret"))

    # s3 bucket settings
    s3_bucket_name: str = Field(os.environ.get("AWS_S3_BUCKET_NAME", "your-s3-bucket-name"))
    s3_region: str = Field(os.environ.get("AWS_S3_REGION", "us-east-1"))
    aws_s3_endpoint_url: str = Field(os.environ.get("AWS_S3_ENDPOINT_URL", None))

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
