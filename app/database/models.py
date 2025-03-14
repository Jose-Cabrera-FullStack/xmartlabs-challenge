import datetime
import uuid
from enum import Enum
from typing import Optional

import ormar

from app.database.config import BaseMeta


class FileType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


class FileStatus(str, Enum):
    PENDING = "pending"
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class FileStorage(ormar.Model):
    class Meta(BaseMeta):
        tablename = "file_storage"

    id: int = ormar.Integer(primary_key=True)
    uuid: str = ormar.String(max_length=36, default=lambda: str(uuid.uuid4()))
    name: str = ormar.String(max_length=255)
    type: FileType = ormar.String(max_length=10, choices=list(FileType))
    size: int = ormar.Integer()
    status: FileStatus = ormar.String(
        max_length=20,
        choices=list(FileStatus),
        default=FileStatus.PENDING
    )
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.utcnow)
    updated_at: Optional[datetime.datetime] = ormar.DateTime(nullable=True)
