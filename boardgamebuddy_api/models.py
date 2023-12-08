from django.db import models

#Users
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#BoardGames
# class BoardGame(models.Model):
#     bgg_id = models.IntegerField()
#     title = models.CharField(max_length=500)
#     cover_image = models.CharField(max_length=500, null=True, blank=True)
#     min_players = models.IntegerField(null=True, blank=True)
#     max_players = models.IntegerField(null=True, blank=True)
#     min_playtime = models.IntegerField(null=True, blank=True)
#     max_playtime = models.IntegerField(null=True, blank=True)
#     categories = models.CharField(max_length=500, null=True, blank=True)
#     cooperative = models.BooleanField()
#     description = models.CharField(max_length=100000, null=True, blank=True)
#     year_published = models.IntegerField(null=True, blank=True)
#     rating = models.FloatField(null=True, blank=True)
#     rank = models.IntegerField(null=True, blank=True)
#     abstracts_rank = models.IntegerField(null=True, blank=True)
#     cgs_rank = models.IntegerField(null=True, blank=True)
#     childrens_games_rank = models.IntegerField(null=True, blank=True)
#     family_games_rank = models.IntegerField(null=True, blank=True)
#     party_games_rank = models.IntegerField(null=True, blank=True)
#     strategy_games_rank = models.IntegerField(null=True, blank=True)
#     thematic_rank = models.IntegerField(null=True, blank=True)
#     wargames_rank = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.title
    
#UserBoardGames
class UserBoardGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_game_id = models.IntegerField()
