from datetime import date
from ninja import Schema
from .models import Author, Publisher
from pydantic import Field
from author.schema import AuthorOutSchema
from publisher.schema import PublisherOutSchema


class BookInSchema(Schema):
    title: str
    publish_date: date
    price: float
    rating :int
    author_id: int = Field(alias='author')
    publisher_id: int = Field(alias='publisher')


class BookOutSchema(Schema):
    id: int
    title: str
    publish_date: date
    price: float
    rating: int
    author: AuthorOutSchema
    publisher: PublisherOutSchema


class BookUpdateSchema(Schema):
    title: str = None
    publish_date: date = None
    price: float = None
    rating: int = None


class Error(Schema):
    message: str