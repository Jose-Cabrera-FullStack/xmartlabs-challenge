import pytest
from unittest.mock import patch

from app.database.models import FileStatus
from app.service.presigned_url import PresignedURLService


class TestPresignedURLService:
    @staticmethod
    async def create_presigned_url(filename, type, file_size):
        content_type = {"image": "image/jpeg", "video": "video/mp4"}.get(type)
        mock_uuid = "mock-uuid-123"
        mock_status = FileStatus.PENDING

        from app.settings import settings
        from app.infrastructure.s3 import generate_presigned_url

        presigned_response = generate_presigned_url(
            bucket_name=settings.s3_bucket_name,
            key=filename,
            content_type=content_type,
            file_size=file_size,
            region=settings.s3_region,
        )

        return {
            "url": presigned_response["url"],
            "key": mock_uuid,
            "status": mock_status
        }


@pytest.mark.asyncio
async def test_create_presigned_url():
    with patch("app.service.presigned_url.PresignedURLService.create_presigned_url", 
               TestPresignedURLService.create_presigned_url), \
         patch("app.infrastructure.s3.generate_presigned_url") as mock_generate_presigned_url:

        mock_generate_presigned_url.return_value = {
            "url": "mocked_url", 
            "fields": {"key": "mocked_key"}
        }

        response = await PresignedURLService.create_presigned_url(
            filename="test.jpg", type="image", file_size=1024
        )

        assert response == {
            "url": "mocked_url", 
            "key": "mock-uuid-123", 
            "status": FileStatus.PENDING
        }

        mock_generate_presigned_url.assert_called_once_with(
            bucket_name="your-s3-bucket-name",
            key="test.jpg",
            content_type="image/jpeg",
            file_size=1024,
            region="us-east-1"
        )


@pytest.mark.asyncio
async def test_create_presigned_url_exception():
    with patch("app.service.presigned_url.PresignedURLService.create_presigned_url", 
               TestPresignedURLService.create_presigned_url), \
         patch("app.infrastructure.s3.generate_presigned_url") as mock_generate_presigned_url:

        mock_generate_presigned_url.side_effect = Exception("Simulated exception")

        with pytest.raises(Exception) as exc_info:
            await PresignedURLService.create_presigned_url(
                filename="test.jpg", type="image", file_size=1024
            )

        assert "Simulated exception" in str(exc_info.value)
