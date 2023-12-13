from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import Note
from .serializers import NoteSerializer, UserSerializer


def home_page_view(request):
    return HttpResponse("<h1>transcriber backend</h1>")


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


class NotesListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # -- LIST
    def get(self, request, *args, **kwargs):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #  -- CREATE
    def post(self, request, *args, **kwargs):
        data = {
            "note": request.data.get("note"),
            "timestamp": request.data.get("timestamp"),
            # 'user': request.user.id
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
