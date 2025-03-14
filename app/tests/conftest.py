import pytest
from unittest.mock import patch, AsyncMock

@pytest.fixture(autouse=True)
async def mock_db_connection():
    """Mock database connection for all tests"""
    with patch("app.database.config.database") as mock_db, \
         patch("ormar.models.model.Model.save", new_callable=AsyncMock) as mock_save, \
         patch("ormar.models.model.Model.update", new_callable=AsyncMock) as mock_update:
        
        # Set up the database mock
        mock_db.is_connected = True
        mock_db.execute = AsyncMock(return_value=1)  # Simulate successful query execution
        mock_db.fetch_val = AsyncMock(return_value=1)
        
        # Configure ORM mocks
        mock_save.return_value = None
        mock_update.return_value = None
        
        yield
