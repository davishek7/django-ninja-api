from ninja import Schema


class PublisherInSchema(Schema):
    name: str


class PublisherOutSchema(Schema):
    id: int
    name: str