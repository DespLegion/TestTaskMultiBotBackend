# Generated by Django 5.0.3 on 2024-03-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('user_username', models.CharField()),
                ('user_firstname', models.CharField()),
                ('user_lastname', models.CharField(null=True)),
                ('user_add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Bot User',
                'verbose_name_plural': 'Bot Users',
            },
        ),
    ]
