# Generated by Django 4.2 on 2024-11-11 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_remove_report_unique_report_per_user_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mentioned_users',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tagged_users',
        ),
        migrations.AddField(
            model_name='post',
            name='tagged_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagged_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
