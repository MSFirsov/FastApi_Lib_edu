import uuid
from datetime import date, datetime

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field, Column


class Book(SQLModel, table=True):
    __tablename__ = 'api_books'

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )

    title: str
    author: str
    description: str
    published_date: date
    price: int
    language: str

    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f'<Book {self.title}>'
