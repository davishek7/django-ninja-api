from django.test import TestCase
from .models import Book, Author, Publisher
# Create your tests here.

class BookTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Author 3')
        self.publisher = Publisher.objects.create(name='Publisher 3')
        self.book = Book.objects.create(title = 'Book 7', price=10.99, rating=8, publish_date="2023-05-02", author = self.author, publisher = self.publisher)

    def test_book_title(self):
        self.assertEqual(self.book.title, 'Book 7')

    def test_book_price(self):
        self.assertEqual(self.book.price, 10.99)

    def test_book_rating(self):
        self.assertEqual(self.book.rating, 8)

    def test_book_author(self):
        self.assertEqual(self.book.author.name, 'Author 3')

    def test_book_publisher(self):
        self.assertEqual(self.book.publisher.name, 'Publisher 3')