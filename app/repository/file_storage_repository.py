import datetime
from typing import Optional

from ormar import NoMatch

from app.database.models import FileStorage, FileStatus


class FileStorageRepository:
    """
    Repository for handling file storage operations in the database.

    This class provides static methods to interact with the FileStorage model,
    including creating new file records and updating their statuses.
    """

    @staticmethod
    async def create_file(name: str, type: str, size: int, status: str = FileStatus.PENDING) -> FileStorage:
        """
        Create a new file record in the database.

        Args:
            name: The name of the file
            type: The type of the file (e.g., 'image', 'video')
            size: The size of the file in bytes
            status: The initial status of the file (default: PENDING)

        Returns:
            The created FileStorage object
        """
        file_storage = await FileStorage.objects.create(
            name=name,
            type=type,
            size=size,
            status=status
        )
        return file_storage

    @staticmethod
    def update_file_status(uuid: str, status: str) -> Optional[FileStorage]:
        """
        Update the status of a file identified by UUID.

        Args:
            uuid: The UUID of the file
            status: The new status to set

        Returns:
            The updated FileStorage object or None if not found
        """
        try:
            file = FileStorage.objects.get(uuid=uuid)
            file.status = status
            file.updated_at = datetime.datetime.utcnow()
            file.update()
            return file
        except NoMatch:
            return None
