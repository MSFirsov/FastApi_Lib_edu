from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.books.routes import books_routes
from src.db.main import db_init


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f'Сервер работает.')
    await db_init()
    yield
    print('Сервер остановился.')


version = 'v1'

app = FastAPI(
    title='LibraryAPI',
    version=version,
    lifespan=life_span,
)

app.include_router(books_routes, prefix=f'/api/{version}/books', tags=['Books'])