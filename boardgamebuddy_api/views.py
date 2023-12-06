from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .serializers import BoardGameSerializer
from .models import *

@api_view(['GET'])
def game_list(request):
    if request.method == 'GET':
        games = BoardGame.objects.all()
        serializer = BoardGameSerializer(games, many=True)
        return Response({"data": serializer.data})

def test(request):
    return HttpResponse("Hello World")