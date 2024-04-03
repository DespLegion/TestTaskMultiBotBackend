# Generated by Django 5.0.3 on 2024-03-31 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot_users', '0003_alter_botuser_user_add_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(verbose_name='Task Title')),
                ('task_text', models.TextField(verbose_name='Task Text')),
                ('task_add_date', models.DateTimeField(auto_now_add=True, verbose_name='Task add date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_users.botuser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Task',
                'verbose_name_plural': 'User Tasks',
            },
        ),
    ]