from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .models import Folder
from .serializers import FolderSerializer


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class that allows only the owner of the note
    to modify it, while allowing authenticated users to perform read it.
    This allows the possibility of shared folders as a future feature.

    Methods:

    * `has_permission(request, view)`:
        - Returns True if the user is authenticated, or False if not.
    * `has_object_permission(request, view, obj)`:
        - Returns True if the user is the owner of the object, or False if not.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class FoldersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows folders to be viewed or edited.

    Methods:

    * `get_queryset(self)`:
        - Returns only the folders owned by the user.
    """

    serializer_class = FolderSerializer
    permission_classes = [OwnerOrReadOnly]
    queryset = Folder.objects.all()

    def get_queryset(self):
        logged_in_user = self.request.user
        return Folder.objects.filter(
            user=logged_in_user.id).order_by("-created_on")
