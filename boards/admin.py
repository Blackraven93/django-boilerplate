from django.contrib import admin
from .models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "description",
    )
    # list_filter = []
    search_fields = ("author",)
