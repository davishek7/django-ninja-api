from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min
from django.http import JsonResponse
from .models import Author, Book, Publisher

# Create your views here.

def index(request):
    max_rated_book_by_author = Author.objects.annotate(highest_rated_book = Max('books__rating')).values("name", "books__title", "highest_rated_book")
    max_rated_book_by_publisher = Publisher.objects.annotate(highest_rated_book=Max('books__rating')).values("name", "books__title", "highest_rated_book")
    avg_book_rating_by_author = Author.objects.annotate(avg_rating=Avg('books__rating')).values("name", "avg_rating")
    print(avg_book_rating_by_author)
    return JsonResponse(list(avg_book_rating_by_author), safe=False)