from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import BoardGameSerializer
from .models import *

@api_view(['GET'])
def game_list(request):
    if request.method == 'GET':
        games = BoardGame.objects.all()
        serializer = BoardGameSerializer(games, many=True)
        return JsonResponse({"data": serializer.data})
    
def game_details(request, id):
    if request.method == 'GET':
        try:
            game = BoardGame.objects.get(pk=id)
        except BoardGame.DoesNotExist:
            ### THIS NEEDS TO BE CHANGED!!!
            raise Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BoardGameSerializer(game)
        # import pdb; pdb.set_trace()
        return JsonResponse(serializer.data)
