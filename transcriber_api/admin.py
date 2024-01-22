from django.contrib import admin
from .models import Note, Folder


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "folder_id", "created_on", "updated_on")
    # search_fields = ("", "", "")

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created_on", "updated_on")
    # search_fields = ("", "", "")
