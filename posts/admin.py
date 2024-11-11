# admin.py
from django.contrib import admin
from .models import Post, Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'category', 'created_at')
    search_fields = ('user__username', 'post__title', 'category')
    list_filter = ('category', 'created_at')

admin.site.register(Post)
admin.site.register(Report, ReportAdmin)
