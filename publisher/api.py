from ninja import Router
from .schema import PublisherInSchema, PublisherOutSchema
from typing import List
from book.models import Publisher
from django.shortcuts import get_object_or_404

router = Router()

@router.get('/', response=List[PublisherOutSchema])
def publisher_list(request):
    publishers = Publisher.objects.all()
    return list(publishers)


@router.get('/{publisher_id}', response=PublisherOutSchema)
def publisher_get(request, publisher_id: int):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    return publisher


@router.post('/', response=PublisherOutSchema)
def publisher_post(request, payload: PublisherInSchema):
    publisher = Publisher.objects.create(**payload.dict())
    return publisher