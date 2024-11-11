# Generated by Django 4.2 on 2024-11-11 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_post_mentioned_users_remove_post_tagged_users_and_more'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('spam', 'Spam'), ('inappropriate_content', 'Inappropriate Content'), ('harassment', 'Harassment or Bullying'), ('hate_speech', 'Hate Speech'), ('misinformation', 'Misinformation'), ('copyright_violation', 'Copyright Violation'), ('impersonation', 'Impersonation'), ('self_harm', 'Self-harm or Suicide'), ('other', 'Other')], default='spam', max_length=50),
        ),
    ]