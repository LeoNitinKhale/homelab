from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_on', 'related_kind', 'related_id')
    list_filter = ('status',)
    search_fields = ('title',)
