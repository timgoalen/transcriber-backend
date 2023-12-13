from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Note
from .serializers import NoteSerializer


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
            'note': request.data.get('note'), 
            'timestamp': request.data.get('timestamp'), 
            # 'user': request.user.id
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)