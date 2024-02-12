from django.urls import re_path as url
from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


# Wire up API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
