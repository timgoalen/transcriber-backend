from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import Note, Folder
from .serializers import NoteSerializer, FolderSerializer, UserSerializer


# def home_page_view(request):
    # return HttpResponse("<h1>transcriber backend</h1>")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """

    queryset = Note.objects.all().order_by("-created_on")
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoldersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows folders to be viewed or edited.
    """

    queryset = Folder.objects.all().order_by("-created_on")
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

