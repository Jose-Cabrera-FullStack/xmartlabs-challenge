from unittest.mock import patch
import sqlalchemy
from app.database import config
import logging

def test_database_connection_success():
    with patch("app.database.config.settings") as mock_settings:
        mock_settings.db_url = "sqlite:///test.db"
        config.database = config.databases.Database(mock_settings.db_url)
        config.engine = sqlalchemy.create_engine(mock_settings.db_url)
        config.metadata.create_all(config.engine)
        assert str(config.database.url) == "sqlite:///test.db"

# def test_database_connection_failure():
#     with patch("app.database.config.settings") as mock_settings, \
#             patch("sqlalchemy.create_engine") as mock_create_engine, \
#             patch.object(logging, 'warning') as mock_logging:
#         mock_settings.db_url = "postgresql://invalid_url"
#         mock_create_engine.side_effect = sqlalchemy.exc.OperationalError("Connection failed", None, None)
#         try:
#             config.database = config.databases.Database(mock_settings.db_url)
#             config.engine = sqlalchemy.create_engine(mock_settings.db_url)
#         except sqlalchemy.exc.OperationalError:
#             pass
#         mock_logging.assert_called()
