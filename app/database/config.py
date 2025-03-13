import logging
import databases

import ormar
import sqlalchemy
from sqlalchemy.exc import OperationalError

from app.settings import settings

try:
    db_url = settings.db_url
    logging.info(f"Trying to connect to database with URL: {db_url}")
    database = databases.Database(db_url)
    engine = sqlalchemy.create_engine(db_url)
    metadata = sqlalchemy.MetaData()
    metadata.create_all(engine)
except OperationalError as e:
    logging.warning(f"Database connection failed: {str(e)}, falling back to sqlite3")
    fallback_db_url = "sqlite:///fallback_db.sqlite3"
    database = databases.Database(fallback_db_url)
    engine = sqlalchemy.create_engine(fallback_db_url)
    metadata = sqlalchemy.MetaData()
    metadata.create_all(engine)


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
