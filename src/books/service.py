from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from .models import Book
from .schemas import BookCreate


class BookService:

    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at)) # SELECT * FROM BOOKS ORDER BY CREATED_AT
        result = await session.exec(statement)
        return result.all()


    async def get_one_book(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None


    async def create_a_book(self, book_data: BookCreate, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        new_book.published_date = datetime.strptime(book_data_dict['published_date'],'%Y-%m-%d')
        session.add(new_book)
        await session.commit()
        return new_book
