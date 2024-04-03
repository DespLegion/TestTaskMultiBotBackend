from django.contrib import admin
from .models import BotUser


@admin.register(BotUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = (
        "user_username",
        "user_firstname",
        "user_lastname",
        "user_id",
        "user_add_date",
    )
    list_display = (
        "user_username",
        "user_firstname",
        "user_lastname",
        "user_last_loc_name",
        "user_last_loc_lat",
        "user_last_loc_lon",
        "user_id",
        "user_add_date",
    )
    list_filter = (
        "user_username",
        "user_id",
        "user_add_date"
    )
    search_fields = (
        "user_username",
        "user_id",
        "user_firstname",
        "user_lastname"
    )
