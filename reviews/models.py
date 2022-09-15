from django.db import models
from common.models import CommonModel


# Create your models here.
class Review(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board = models.ForeignKey(
        "boards.Board",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    description = models.CharField(max_length=320)

    def __str__(self):
        return f"{self.user}'s review: {self.board}"
