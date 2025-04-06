from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.books.schemas import Book, BookCreate

books_routes = APIRouter()
books_service = BookService()

#__________GET all__________

@books_routes.get('/', response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await books_service.get_all_books(session)
    return books

#__________GET one__________

@books_routes.get('/{book_uid}', response_model=Book)
async def get_one_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    book = await books_service.get_one_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Книги нет'
        )



#______ POST one ________

@books_routes.post('/',status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data: BookCreate, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await books_service.create_a_book(book_data, session)
    return new_book
