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


# users
from .serializers import UserSerializer
from .models import User

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({"data": serializer.data})

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
