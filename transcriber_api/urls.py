# from django.conf.urls import url
from django.urls import re_path as url
from django.urls import path, include
from .views import (
    NotesListApiView,
)

urlpatterns = [
    path('api/', NotesListApiView.as_view(), name="notes-api"),
]