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
