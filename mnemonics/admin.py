from django.contrib import admin

from .models import Peg


@admin.register(Peg)
class PegAdmin(admin.ModelAdmin):
    list_display = ('number', 'word', 'updated_at')
    search_fields = ('word', 'notes')
    ordering = ('number',)
