from pydantic import BaseModel

class PresignedURLRequest(BaseModel):
    filename: str
    content_type: str
    file_size: int
