from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import JsonResponse


def home(request):
    """
    Returns a JSON object with a welcome message.
    """
    data = {"message": "Hi, welcome to the Transcriber REST API"}
    return JsonResponse(data)
