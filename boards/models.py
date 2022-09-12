from django.db import models
from common.models import CommonModel


class Board(CommonModel):
    class BoardCategoryChoices(models.TextChoices):
        DEVELOPMENT = ("dev", "Development")
        DESIGN = ('design', "Design")
        PROJECT_MANAGING = ('PM', 'project manage')
        CULTURE = ('Culture', 'culture')

    """Board Model"""
    board_title = models.CharField(max_length=140)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    description = models.TextField(max_length=140)
    category = models.CharField(max_length=20, choices=BoardCategoryChoices.choices)
    tags = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title
