# from django.conf.urls import url
from django.urls import re_path as url
from django.urls import path, include
from rest_framework import routers

from .views import (
    # NotesListApiView,
    # home_page_view,
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
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += router.urls
