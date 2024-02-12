"""
URL configuration for transcriber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from notes import urls as notes_urls
# from folders import urls as folders_urls

urlpatterns = [
    # path("", include(notes_urls)),
    # path("", include(folders_urls)),
    path("api/auth/", include("authentication.urls")),
    path("admin/", admin.site.urls),
    # Login/logout for browable APIs:
    # TODO: CHECK THIS...
    path("api-auth/", include("rest_framework.urls")),
]
