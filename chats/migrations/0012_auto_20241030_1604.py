# Generated by Django 3.2.4 on 2024-10-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0011_auto_20241030_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.AddField(
            model_name='chat',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]