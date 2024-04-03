from django.db import models


class BotUser(models.Model):
    user_id = models.BigIntegerField(unique=True, null=False, verbose_name="User ID")
    user_username = models.CharField(null=True, blank=True, verbose_name="Username")
    user_firstname = models.CharField(null=False, verbose_name="Firstname")
    user_lastname = models.CharField(null=True, blank=True, verbose_name="Lastname")

    user_add_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")

    user_last_loc_name = models.CharField(null=True, blank=True, verbose_name="Last located city")
    user_last_loc_lat = models.FloatField(null=True, blank=True, verbose_name="Last located latitude")
    user_last_loc_lon = models.FloatField(null=True, blank=True, verbose_name="Last located longitude")

    def __str__(self):
        return self.user_firstname

    class Meta:
        verbose_name = "Bot User"
        verbose_name_plural = "Bot Users"
