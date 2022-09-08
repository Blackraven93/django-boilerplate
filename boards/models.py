from django.db import models


class Board(models.Model):
    """Board Model"""

    title = models.CharField(max_length=140)
    author = models.CharField(max_length=20)
    description = models.TextField(max_length=140)

    def __str__(self):
        return self.title

