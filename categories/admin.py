from django.contrib import admin
from .models import BookCategory
from .models import BoardCategory

# Register your models here.
@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind"
    )

    list_filter = ("kind", )


@admin.register(BoardCategory)
class BoardCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind"
    )

    list_filter = ("kind", )
    search_fields = ("name",)
