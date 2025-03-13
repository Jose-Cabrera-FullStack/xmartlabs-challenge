from unittest.mock import patch
from app.service.presigned_url import PresignedURLService
import pytest

def test_create_presigned_url():
    with patch("app.service.presigned_url.generate_presigned_url") as mock_generate_presigned_url:
        mock_generate_presigned_url.return_value = {"url": "mocked_url", "fields": {"key": "mocked_key"}}
        response = PresignedURLService.create_presigned_url(
            filename="test.jpg", content_type="image/jpeg", file_size=1024
        )
        assert response == {"url": "mocked_url", "fields": {"key": "mocked_key"}}
        mock_generate_presigned_url.assert_called_once_with(
            bucket_name="your-s3-bucket-name",
            key="test.jpg",
            content_type="image/jpeg",
            file_size=1024,
            region="us-east-1"
        )

def test_create_presigned_url_exception():
    with patch("app.service.presigned_url.generate_presigned_url") as mock_generate_presigned_url:
        mock_generate_presigned_url.side_effect = Exception("Simulated exception")
        with pytest.raises(Exception, match="Simulated exception"):
            PresignedURLService.create_presigned_url(
                filename="test.jpg", content_type="image/jpeg", file_size=1024
            )
