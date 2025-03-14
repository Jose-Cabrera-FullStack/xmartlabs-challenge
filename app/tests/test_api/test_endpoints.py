from unittest.mock import patch, AsyncMock, MagicMock
from datetime import datetime
from uuid import UUID

from fastapi.testclient import TestClient

from app.main import app
from app.database.models import FileStatus

client = TestClient(app)


def test_create_presigned_url_endpoint():
    with patch("app.service.presigned_url.PresignedURLService.create_presigned_url") as mock_create_presigned_url:
        mock_create_presigned_url.return_value = {
            "url": "mocked_url",
            "key": "mock-uuid-123",
            "status": "pending"
        }
        response = client.post(
            "/presigned-url",
            json={"filename": "test.jpg", "type": "image", "file_size": 1024}
        )

        assert response.status_code == 200
        assert response.json() == {
            "url": "mocked_url",
            "key": "mock-uuid-123",
            "status": "pending"
        }
        mock_create_presigned_url.assert_called_once_with("test.jpg", "image", 1024)


def test_update_file_status_endpoint():
    valid_status = FileStatus.UPLOADED.value
    mock_uuid = "f47ac10b-58cc-4372-a567-0e02b2c3d479"

    mock_file = MagicMock()
    mock_file.uuid = UUID(mock_uuid)
    mock_file.name = "test-file.jpg"
    mock_file.type = "image"
    mock_file.status = valid_status
    mock_file.updated_at = datetime.now()

    with patch("app.service.file_storage.FileStorageService.update_file_status", new_callable=AsyncMock) as mock_update_status:
        mock_update_status.return_value = mock_file

        response = client.put(
            "/file-status",
            json={"uuid": mock_uuid, "status": valid_status}
        )

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["uuid"] == mock_uuid
        assert response_data["status"] == valid_status
        assert "name" in response_data
        assert "type" in response_data
        assert "updated_at" in response_data

        mock_update_status.assert_awaited_once_with(mock_uuid, valid_status)
