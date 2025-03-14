from unittest.mock import patch
import uuid
from datetime import datetime

import pytest

from app.database.models import FileStorage
from app.service.file_storage import FileStorageService


@pytest.mark.asyncio
async def test_update_file_status_success():
    mock_uuid = str(uuid.uuid4())
    mock_file = FileStorage(
        uuid=mock_uuid,
        name="test_file.jpg",
        type="image",
        status="uploaded",
        size=1024,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    with patch("app.repository.FileStorageRepository.update_file_status") as mock_update:
        mock_update.return_value = mock_file
        result = await FileStorageService.update_file_status(mock_uuid, "uploaded")
        mock_update.assert_called_once_with(mock_uuid, "uploaded")
        assert result == mock_file
        assert result.status == "uploaded"


@pytest.mark.asyncio
async def test_update_file_status_not_found():
    with patch("app.repository.FileStorageRepository.update_file_status") as mock_update:
        mock_update.return_value = None
        with pytest.raises(ValueError, match="File not found"):
            await FileStorageService.update_file_status("non-existent-uuid", "uploaded")
        mock_update.assert_called_once_with("non-existent-uuid", "uploaded")


@pytest.mark.asyncio
async def test_update_file_status_exception():
    with patch("app.repository.FileStorageRepository.update_file_status") as mock_update:
        mock_update.side_effect = Exception("Database error")
        with pytest.raises(Exception, match="Database error"):
            await FileStorageService.update_file_status("some-uuid", "uploaded")
        mock_update.assert_called_once_with("some-uuid", "uploaded")
