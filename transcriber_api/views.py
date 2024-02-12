from django.contrib.auth.models import Group, User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import Note, Folder
from .serializers import NoteSerializer, FolderSerializer, UserSerializer


class OwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [OwnerOrReadOnly]

    def get_queryset(self):
        logged_in_user = self.request.user
        return User.objects.filter(id=logged_in_user.id)


class NotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """

    serializer_class = NoteSerializer
    permission_classes = [OwnerOrReadOnly]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Note.objects.all()

    def get_queryset(self):
        logged_in_user = self.request.user
        return Note.objects.filter(user=logged_in_user.id).order_by("-created_on")


class FoldersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows folders to be viewed or edited.
    """

    serializer_class = FolderSerializer
    permission_classes = [OwnerOrReadOnly]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Folder.objects.all()

    def get_queryset(self):
        logged_in_user = self.request.user
        return Folder.objects.filter(user=logged_in_user.id).order_by("-created_on")
