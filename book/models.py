from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    price = models.FloatField()
    rating = models.SmallIntegerField()
    author = models.ForeignKey("Author", related_name="books", on_delete=models.CASCADE)
    publisher = models.ForeignKey("Publisher", related_name="books", on_delete=models.CASCADE)
    

class Author(models.Model):
    name = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)