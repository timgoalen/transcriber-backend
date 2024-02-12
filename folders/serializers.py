from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Folder


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Folder
        fields = ["id", "user", "title", "colour", "created_on", "updated_on"]
