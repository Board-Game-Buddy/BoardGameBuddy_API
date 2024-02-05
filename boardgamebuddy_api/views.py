from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
# from datetime import timedelta
import pdb


from .serializers import *
from .models import *
from .facades import BoardGamesFacade

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
        cache.set("all_users", serializer.data, 30)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def user_details(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
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

@api_view(['GET', 'POST', 'DELETE'])
def user_boardgames(request, id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        user_board_games = UserBoardGame.objects.filter(user=user.id)
        bg_count = len(user_board_games)
        if cache.get(f"user_favorites{bg_count}") == None:
            board_game_ids = [game.board_game_id for game in user_board_games]
            board_games = BoardGamesFacade(board_game_ids).get_board_game_data()
            serializer = BoardGameSerializer(board_games, many=True)
            cache.set(f"user_favorites{bg_count}", serializer.data, 30)
            return JsonResponse(serializer.data, safe = False)
        else:
            return JsonResponse(cache.get(f"user_favorites{bg_count}"), safe = False)
        
    elif request.method == 'POST':
        board_game_id = request.GET.get('board_game_id')
        data = {
            'user': id,
            'board_game_id': board_game_id
        }
        serializer = UserBoardGameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user = id
        board_game_id = request.GET.get('board_game_id')
        user_board_game = UserBoardGame.objects.filter(user=user).filter(board_game_id=board_game_id)
        user_board_game.delete()
        return Response("User Favorite Deleted", status=status.HTTP_204_NO_CONTENT)
