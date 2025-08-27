from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from core.config import settings

DATABASE_URL = settings.database.get_db_url()


engine = create_async_engine(
    url=DATABASE_URL,
)
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
