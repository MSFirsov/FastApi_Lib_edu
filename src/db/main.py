from sqlmodel import SQLModel
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

#Создаем движок на основе config.py

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

async def db_init():
    async with engine.begin() as connection:
        from src.books.models import Book

        await connection.run_sync(SQLModel.metadata.create_all)



async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
