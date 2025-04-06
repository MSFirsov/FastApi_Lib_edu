import uuid
from datetime import date, datetime

from pydantic import BaseModel

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    description: str
    published_date: date
    price: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    published_date: str
    price: int
    language: str