from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .serializers import UserSerializer


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
    permission_classes = [OwnerOrReadOnly]

    def get_queryset(self):
        logged_in_user = self.request.user
        return User.objects.filter(id=logged_in_user.id)
