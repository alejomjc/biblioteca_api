from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    isbn: Optional[str] = None


class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
