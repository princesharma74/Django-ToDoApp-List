from django.contrib import admin
from .models import Tag, Task

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the 'name' field in the admin list view

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)  # Make the 'timestamp' field read-only in the admin interface
    list_display = ('title', 'status')  # Display the 'title' and 'status' fields in the admin list view
    list_filter = ('status',)  # Add a filter option for the 'status' field in the admin list view
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'due_date', 'status')  # Group the fields under the 'General' section
        }),
        ('Tags', {
            'fields': ('tags',)  # Group the 'tags' field under the 'Tags' section
        }),
    )
