from django.db import models
from common.models import CommonModel


# Create your models here.

class BookCategory(CommonModel):
    class BookCategoryKindChoices(models.TextChoices):
        IT = ("dev", "Development")
        DESIGN = ('design', "Design")
        BUSINESS = ('PM', 'project manage')

    name = models.CharField(max_length=40)
    kind = models.CharField(max_length=15, choices=BookCategoryKindChoices.choices)

    def __str__(self):
        return f"{self.kind}: {self.name}"


class BoardCategory(CommonModel):
    class BoardCategoryKindChoices(models.TextChoices):
        DEVELOPMENT = ("dev", "Development")
        DESIGN = ('design', "Design")
        PROJECT_MANAGING = ('PM', 'project manage')
        CULTURE = ('Culture', 'culture')

    name = models.CharField(max_length=40)
    kind = models.CharField(max_length=15, choices=BoardCategoryKindChoices.choices)

    def __str__(self):
        return f"{self.kind}: {self.name}"

