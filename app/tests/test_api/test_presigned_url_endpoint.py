from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
import json

client = TestClient(app)

def test_create_presigned_url_endpoint():
    with patch("app.service.presigned_url.PresignedURLService.create_presigned_url") as mock_create_presigned_url:
        mock_create_presigned_url.return_value = {"url": "mocked_url", "fields": {"key": "mocked_key"}}
        response = client.post(
            "/presigned-url",
            json={"filename": "test.jpg", "content_type": "image/jpeg", "file_size": 1024}
        )
        assert response.status_code == 200
        assert response.json() == {"url": "mocked_url", "fields": {"key": "mocked_key"}}
        mock_create_presigned_url.assert_called_once_with("test.jpg", "image/jpeg", 1024)
