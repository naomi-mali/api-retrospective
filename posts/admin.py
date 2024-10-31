# admin.py
from django.contrib import admin
from .models import Post, Report

class ReportAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('post', 'user', 'category', 'created_at', 'reason')
    # Fields that can be searched
    search_fields = ('user__username', 'post__title', 'reason')
    # Allow filtering by category
    list_filter = ('category', 'created_at')
    # Optionally, allow sorting by created_at
    ordering = ('-created_at',)

# Register the models with the admin site
admin.site.register(Post)
admin.site.register(Report, ReportAdmin)
