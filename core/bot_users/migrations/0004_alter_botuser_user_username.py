# Generated by Django 5.0.3 on 2024-04-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0003_alter_botuser_user_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='user_username',
            field=models.CharField(blank=True, null=True, verbose_name='Username'),
        ),
    ]
