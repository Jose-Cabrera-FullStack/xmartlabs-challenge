from unittest.mock import patch
import sqlalchemy
from app.database import config


def test_database_connection_success():
    with patch("app.database.config.settings") as mock_settings:
        mock_settings.db_url = "sqlite:///test.db"
        config.database = config.databases.Database(mock_settings.db_url)
        config.engine = sqlalchemy.create_engine(mock_settings.db_url)
        config.metadata.create_all(config.engine)
        assert str(config.database.url) == "sqlite:///test.db"
