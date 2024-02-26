from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .models import Prompt
from .serializers import PromptSerializer


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class that allows only the owner of the prompt
    to modify it, while allowing authenticated users to perform read it.

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


class PromptsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prompts to be viewed or edited.

    Methods:

    * `get_queryset(self)`:
        - Returns only the prompts owned by the user.
    """

    serializer_class = PromptSerializer
    permission_classes = [OwnerOrReadOnly]
    queryset = Prompt.objects.all()

    def get_queryset(self):
        logged_in_user = self.request.user
        return Prompt.objects.filter(user=logged_in_user.id).order_by("-created_on")
