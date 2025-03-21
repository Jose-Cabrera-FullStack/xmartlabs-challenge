from pydantic import BaseModel, validator

from app.database.models import FileStatus


class UpdateFileStatusRequest(BaseModel):
    uuid: str
    status: str

    @validator('uuid')
    def validate_uuid(cls, uuid):
        if not uuid:
            raise ValueError('uuid must not be empty')
        return uuid

    @validator('status')
    def validate_status(cls, status):
        valid_statuses = [s.value for s in FileStatus]
        if status not in valid_statuses:
            raise ValueError(f'status must be one of {valid_statuses}')
        return status

    class Config:
        schema_extra = {
            "example": {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "status": "uploaded"
            }
        }
