from pydantic import BaseModel


class PresignedURLResponse(BaseModel):
    url: str
    key: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "url": "https://your-bucket.s3.amazonaws.com",
                "key": "123e4567-e89b-12d3-a456-426614174000",
                "status": "pending"
            }
        }
