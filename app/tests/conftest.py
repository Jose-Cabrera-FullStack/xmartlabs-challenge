import pytest
from unittest.mock import patch, AsyncMock

@pytest.fixture(autouse=True)
async def mock_db_connection():
    """Mock database connection for all tests"""
    with patch("app.database.config.database") as mock_db, \
         patch("app.database.models.FileStorage.objects") as mock_objects, \
         patch("ormar.models.model.Model.save", new_callable=AsyncMock), \
         patch("ormar.models.model.Model.update", new_callable=AsyncMock):

        mock_db.is_connected = True
        mock_db.execute = AsyncMock(return_value=1)
        mock_db.fetch_val = AsyncMock(return_value=1)

        mock_objects.create = AsyncMock()
        mock_objects.get = AsyncMock()
        mock_objects.filter = AsyncMock()
        mock_objects.all = AsyncMock()

        yield
