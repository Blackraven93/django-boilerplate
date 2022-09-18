from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
    )
    list_filter = (
        'user__is_host',
    )
