from ninja import Schema


class AuthorInSchema(Schema):
    name: str


class AuthorOutSchema(Schema):
    id: int
    name: str