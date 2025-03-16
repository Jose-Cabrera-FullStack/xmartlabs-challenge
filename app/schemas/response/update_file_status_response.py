from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class UpdateFileStatusResponse(BaseModel):
    uuid: UUID
    name: str
    type: str
    status: str
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "vacation_photo.jpg",
                "type": "image/jpeg",
                "status": "uploaded",
                "updated_at": "2025-03-16T13:45:30.123456"
            }
        }
