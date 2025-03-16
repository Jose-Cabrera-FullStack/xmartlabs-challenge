from unittest.mock import patch, AsyncMock, MagicMock

import pytest

from app.database.models import FileStatus
from app.service.presigned_url import PresignedURLService


@pytest.mark.asyncio
async def test_create_presigned_url():
    mock_file = MagicMock()
    mock_file.uuid = "mock-uuid-123"
    mock_file.status = FileStatus.PENDING

    with patch("app.repository.file_storage_repository.FileStorageRepository.create_file", new_callable=AsyncMock) as mock_create_file, patch("app.service.presigned_url.generate_presigned_url") as mock_generate_presigned_url:

        mock_create_file.return_value = mock_file
        mock_generate_presigned_url.return_value = {"url": "mocked_url", "fields": {"key": "mocked_key"}}

        response = await PresignedURLService.create_presigned_url(filename="test.jpg", type="image", file_size=1024)
        assert response == {"url": "mocked_url", "key": "mock-uuid-123", "status": FileStatus.PENDING}

        mock_create_file.assert_called_once_with(name="test.jpg", type="image", size=1024)
        mock_generate_presigned_url.assert_called_once_with(bucket_name="your-s3-bucket-name", key="test.jpg", content_type="image/jpeg", file_size=1024, region="us-east-1")


@pytest.mark.asyncio
async def test_create_presigned_url_exception():
    mock_file = MagicMock()
    mock_file.uuid = "mock-uuid-123"
    mock_file.status = FileStatus.PENDING

    with patch("app.repository.file_storage_repository.FileStorageRepository.create_file", new_callable=AsyncMock) as mock_create_file, patch("app.service.presigned_url.generate_presigned_url") as mock_generate_presigned_url:

        mock_create_file.return_value = mock_file
        mock_generate_presigned_url.side_effect = Exception("Simulated exception")

        with pytest.raises(Exception) as exc_info:
            await PresignedURLService.create_presigned_url(filename="test.jpg", type="image", file_size=1024)

        assert "Simulated exception" in str(exc_info.value)
        mock_create_file.assert_called_once()
