from django.contrib import admin
from .models import WatermarkModel


@admin.register(WatermarkModel)
class CustomWatermarkAdmin(admin.ModelAdmin):
    readonly_fields = (
        "id",
    )
    list_display = (
        "watermark_img",
    )
    list_filter = (
        "id",
        "user",
    )
    search_fields = (
        "user",
    )
