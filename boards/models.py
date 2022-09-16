from django.db import models
from common.models import CommonModel


class Board(CommonModel):

    """Board Model"""
    board_title = models.CharField(max_length=140)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    description = models.TextField(max_length=140)
    category = models.ForeignKey("categories.BoardCategory", null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.CharField(max_length=120)
    private = models.BooleanField(default=False)
    view = models.IntegerField(null=True)

    def __str__(self):
        return self.board_title

    def total_category(self):
        return self.category.count()

