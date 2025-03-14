import pytest
from unittest.mock import patch, MagicMock, AsyncMock

from app.database.models import FileStatus
from app.service.presigned_url import PresignedURLService


@pytest.mark.asyncio
async def test_create_presigned_url():
    # Mock the entire database connection
    with patch("app.database.config.database") as mock_db, \
         patch("app.database.models.FileStorage.objects.create", new_callable=AsyncMock) as mock_create, \
         patch("app.service.presigned_url.generate_presigned_url") as mock_generate_presigned_url:
        
        # Set up database mock to avoid connection issues
        mock_db.is_connected = True
        
        # Create a mock file storage object
        mock_file = MagicMock()
        mock_file.uuid = "mock-uuid-123"
        mock_file.status = FileStatus.PENDING
        mock_create.return_value = mock_file
        
        # Mock the presigned URL generation
        mock_generate_presigned_url.return_value = {
            "url": "mocked_url", 
            "fields": {"key": "mocked_key"}
        }
        
        # Call async function with await
        response = await PresignedURLService.create_presigned_url(
            filename="test.jpg", type="image", file_size=1024
        )
        
        # Assert the new response format
        assert response == {
            "url": "mocked_url", 
            "key": "mock-uuid-123", 
            "status": FileStatus.PENDING
        }
        
        # Verify the mocks were called correctly
        mock_create.assert_called_once()
        mock_generate_presigned_url.assert_called_once()


@pytest.mark.asyncio
async def test_create_presigned_url_exception():
    # Mock the entire database connection
    with patch("app.database.config.database") as mock_db, \
         patch("app.database.models.FileStorage.objects.create", new_callable=AsyncMock) as mock_create, \
         patch("app.service.presigned_url.generate_presigned_url") as mock_generate_presigned_url:
        
        # Set up database mock to avoid connection issues
        mock_db.is_connected = True
        
        # Set up the database mock to succeed
        mock_file = MagicMock()
        mock_file.uuid = "mock-uuid-123"
        mock_file.status = FileStatus.PENDING
        mock_create.return_value = mock_file
        
        # Make the presigned URL generation fail with a specific exception
        mock_generate_presigned_url.side_effect = Exception("Simulated exception")
        
        # Test with proper exception handling
        with pytest.raises(Exception) as exc_info:
            await PresignedURLService.create_presigned_url(
                filename="test.jpg", type="image", file_size=1024
            )
        
        # Verify we get the right exception
        assert "Simulated exception" in str(exc_info.value)
