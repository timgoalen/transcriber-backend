# from django.contrib.auth.models import User
# from rest_framework import permissions, viewsets
# # from .models import Folder
# from .serializers import FolderSerializer


# class OwnerOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return True
#         return False

#     def has_object_permission(self, request, view, obj):
#         if obj.user == request.user:
#             return True
#         return False


# # class FoldersViewSet(viewsets.ModelViewSet):
# #     """
# #     API endpoint that allows folders to be viewed or edited.
# #     """

# #     serializer_class = FolderSerializer
# #     permission_classes = [OwnerOrReadOnly]
# #     queryset = Folder.objects.all()

# #     def get_queryset(self):
# #         logged_in_user = self.request.user
# #         return Folder.objects.filter(user=logged_in_user.id).order_by("-created_on")
