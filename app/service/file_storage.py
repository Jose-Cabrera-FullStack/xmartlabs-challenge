from typing import Optional

from app.database.models import FileStorage
from app.repository import FileStorageRepository


class FileStorageService:
    """
    Service for handling file storage operations.
    """

    @staticmethod
    async def update_file_status(uuid: str, status: str) -> Optional[FileStorage]:
        """
        Update the status of a file identified by UUID.

        Args:
            uuid: The UUID of the file
            status: The new status to set

        Returns:
            The updated FileStorage object or None if not found
        """
        try:
            file = FileStorageRepository.update_file_status(uuid, status)

            if not file:
                raise ValueError('File not found')

            return file
        except ValueError as value_error:
            raise value_error
        except Exception as error:
            raise error
