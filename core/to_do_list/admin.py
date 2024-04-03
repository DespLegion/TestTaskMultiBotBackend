from django.contrib import admin
from .models import TasksModel


@admin.register(TasksModel)
class CustomTasksAdmin(admin.ModelAdmin):
    readonly_fields = (
        "user",
        "task_add_date"
    )
    list_display = (
        "task_title",
        "task_text"
    )
    list_filter = (
        "user",
        "task_add_date"
    )
    search_fields = (
        "user",
        "task_title",
        "task_add_date"
    )
