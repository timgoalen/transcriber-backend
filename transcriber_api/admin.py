from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("note", "timestamp", "created_on", "updated_on")
    # search_fields = ("", "", "")
