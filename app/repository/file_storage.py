import datetime
from typing import Optional

from ormar import NoMatch

from app.database.models import FileStorage


class FileStorageRepository:

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
