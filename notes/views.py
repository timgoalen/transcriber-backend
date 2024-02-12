from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .models import Note
from .serializers import NoteSerializer


class OwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class NotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """

    serializer_class = NoteSerializer
    permission_classes = [OwnerOrReadOnly]
    queryset = Note.objects.all()

    def get_queryset(self):
        logged_in_user = self.request.user
        return Note.objects.filter(user=logged_in_user.id).order_by("-created_on")
