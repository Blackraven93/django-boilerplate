from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.action(description="Init host permission")
def init_host(model_admin, requests, users):
    users.update(is_host=False)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    actions = (init_host,)
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username", "password", "name", "email", "is_host", "avatar", "gender",
                           "language"),
            },
        ),
        ("Permissions",
         {
             "fields": (
                 "is_active",
                 "is_staff",
                 "is_superuser",
                 "groups",
                 "user_permissions",
             ),
         },
         ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "email", "name", "is_host", 'gender')
    search_fields = (
        "username",
        "language",
        "gender",
        "is_host"
    )
