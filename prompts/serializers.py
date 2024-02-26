from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Prompt


class PromptSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Prompt model."""

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Prompt
        fields = ["id", "user", "text", "created_on"]
