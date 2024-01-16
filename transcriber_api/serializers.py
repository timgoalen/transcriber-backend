from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Note

# originally used just 'ModelSerializer':
# class NoteSerializer(serializers.ModelSerializer):


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "text", "folder_id", "created_on", "updated_on"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']