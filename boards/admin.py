from django.contrib import admin
from .models import Board


@admin.action(description="set all board private")
def set_all_private(model_admin, requests, boards):
    boards.update(private=True)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "board_title",
        "author",
        "description",
    )
    list_filter = (
        "board_title",
        "author"
    )
    readonly_fields = (
        "created_at",
        "updated_at"
    )
    search_fields = (
        "^board_title",
        "^author",
        '=author__name'
    )
