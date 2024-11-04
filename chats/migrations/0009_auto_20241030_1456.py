# Generated by Django 3.2.4 on 2024-10-30 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0008_auto_20241030_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]