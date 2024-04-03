from django.db import models


class TasksModel(models.Model):
    task_title = models.CharField(null=False, blank=False, verbose_name="Task Title")
    task_text = models.TextField(null=False, blank=False, verbose_name="Task Text")
    user = models.ForeignKey("bot_users.BotUser", on_delete=models.CASCADE, null=False, blank=False, verbose_name="User")
    task_add_date = models.DateTimeField(auto_now_add=True, verbose_name="Task add date")

    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name = "User Task"
        verbose_name_plural = "User Tasks"
