from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *

### WE ARE PLANNING TO DO ALL BG RELATED CALLS DIRECTLY TO THE MIDDLEMAN
### LEAVING THIS HERE IN CASE THAT CHANGES
# @api_view(['GET'])
# def game_list(request):
#     if request.method == 'GET':
#         games = BoardGame.objects.all()
#         serializer = BoardGameSerializer(games, many=True)
#         return JsonResponse({serializer.data})
    
# def game_details(request, id):
#     if request.method == 'GET':
#         try:
#             game = BoardGame.objects.get(pk=id)
#         except BoardGame.DoesNotExist:
#             ### THIS NEEDS TO BE CHANGED!!!
#             raise JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = BoardGameSerializer(game)
#         return JsonResponse(serializer.data)

# User CRUD
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def user_details(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        raise JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PATCH':
        user_update = UserSerializer(user, data=request.data)
        if user_update.is_valid():
            user_update.save()
            return JsonResponse(user_update.data)
        return JsonResponse(user_update.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response("User Deleted", status=status.HTTP_204_NO_CONTENT)