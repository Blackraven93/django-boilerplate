from django.contrib import admin

# Register your models here.
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "book_title",
        "publisher",
        "category",
        "private",
        "description",
    )

    list_filter = (
        "book_title",
        "publisher",
        "category",
        "private",
    )

    readonly_fields = (
        "created_at",
        "updated_at"
    )

    search_fields = ("book_title",)
