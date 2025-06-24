from ninja import Router
from .models import Book, Author, Publisher
from .schema import BookInSchema, BookOutSchema, BookUpdateSchema
from typing import List
from django.shortcuts import get_object_or_404

router = Router()


@router.post('/', response=BookOutSchema)
def create_book(request, payload: BookInSchema):
    author = get_object_or_404(Author, id=payload.author_id)
    publisher = get_object_or_404(Publisher, id=payload.publisher_id)
    book = Book.objects.create(title=payload.title, publish_date=payload.publish_date, price=payload.price,
                               rating=payload.rating, author=author, publisher=publisher)
    return book


@router.get('/', response=List[BookOutSchema])
def list_books(request):
    books = Book.objects.select_related('author', 'publisher')
    return list(books)


@router.get('/{book_id}', response=BookOutSchema)
def book_details(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@router.put('/{book_id}', response=BookOutSchema)
def book_update(request, book_id: int, payload: BookUpdateSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return {'success': True}


@router.delete('/{book_id}')
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}
