from django.db import models
from common.models import CommonModel


# Create your models here.
class Book(CommonModel):

    """Book Model"""
    book_title = models.CharField(max_length=140, default="")
    publisher = models.CharField(max_length=15)
    category = models.ForeignKey("categories.BookCategory", null=True, blank=True, on_delete=models.SET_NULL)
    private = models.BooleanField(default=False)
    description = models.TextField(max_length=140, null=True, blank=True)
    view = models.IntegerField(null=True)

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name_plural = "Categories"
