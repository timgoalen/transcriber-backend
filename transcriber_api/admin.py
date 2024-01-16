from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("text", "folder_id", "created_on", "updated_on")
    # search_fields = ("", "", "")
