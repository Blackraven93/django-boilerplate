from django.contrib import admin
from .models import Review


class WorldFilter(admin.SimpleListFilter):
    title = "Filter by words"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ('awesome', "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(description__contains=word)
        else:
            reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
    )
    list_filter = (
        'user__is_host',
        'board__view'
    )
