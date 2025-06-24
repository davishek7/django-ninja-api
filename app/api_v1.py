from ninja import NinjaAPI
from book.api import router as book_router

api = NinjaAPI(version='1.0.0')

api.add_router('/books/', "book.api.router", tags=['books'])
api.add_router('/publishers/', "publisher.api.router", tags=['publishers'])
api.add_router('/authors/', "author.api.router", tags=['authors'])