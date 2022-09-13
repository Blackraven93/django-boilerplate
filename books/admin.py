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
        "created_at",
        "updated_at"
    )
    list_filter = (
        "book_title",
        "publisher",
        "category",
        "private",
    )
    search_fields = ("book_title",)
