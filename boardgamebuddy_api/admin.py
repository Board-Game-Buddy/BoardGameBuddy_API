from django.contrib import admin
from .models import BoardGame, User, UserBoardGame

admin.site.register(BoardGame)
admin.site.register(User)
admin.site.register(UserBoardGame)