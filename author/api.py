from django.shortcuts import get_object_or_404
from book.models import Author
from .schema import AuthorInSchema, AuthorOutSchema
from typing import List
from ninja import Router

router = Router()

@router.get('/', response=List[AuthorOutSchema])
def authors_list(request: AuthorInSchema):
    authors = Author.objects.all()
    return list(authors)


@router.get('/{author_id}', response=AuthorOutSchema)
def authors_get(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author


@router.post('/', response=AuthorOutSchema)
def authors_post(request, payload: AuthorInSchema):
    author = Author.objects.create(**payload.dict())
    return author