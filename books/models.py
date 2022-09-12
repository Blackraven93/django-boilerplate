from django.db import models
from common.models import CommonModel

# Create your models here.
class Book(CommonModel):
    class BookCategoryChoices(models.TextChoices):
        IT = ("dev", "Development")
        DESIGN = ('design', "Design")
        BUSINESS = ('PM', 'project manage')

    """Book Model"""
    book_title = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publisher = models.CharField(max_length=15)
    category = models.CharField(max_length=20, choices=BookCategoryChoices.choices)
    private = models.BooleanField(default=False)
    description = models.TextField(max_length=140)
