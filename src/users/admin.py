from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["__str__", "is_staff"]
    ordering = ["email"]
    search_fields = ["email"]

    exclude = ["password"]
    readonly_fields = ["date_joined", "last_login"]
