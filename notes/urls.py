from django.urls import re_path as url
from django.urls import path, include
from rest_framework import routers

from .views import (
    UserViewSet,
    NotesViewSet,
    FoldersViewSet,
)


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"notes", NotesViewSet)
router.register(r"folders", FoldersViewSet)
# router.register(r"groups", views.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    # TODO: this is also in the main urls.py file, choose where needed (maybe add `namespace="rest_framework"` to other)
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += router.urls
