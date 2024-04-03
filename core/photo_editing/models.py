from django.db import models


class WatermarkModel(models.Model):
    watermark_img = models.ImageField(
        upload_to="static/photo_editing/watermarks/",
        default="static/photo_editing/watermarks/logo3.png",
        verbose_name="Watermark Image"
    )
    user = models.ForeignKey("bot_users.BotUser", on_delete=models.CASCADE, null=False, blank=False, verbose_name="User")

    class Meta:
        verbose_name = "User Watermark"
        verbose_name_plural = "Users Watermarks"
