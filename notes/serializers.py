from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Note model."""

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Note
        fields = [
            "id", "user", "text", "folder_id", "created_on", "updated_on"
            ]
