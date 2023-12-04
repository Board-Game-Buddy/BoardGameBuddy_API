from rest_framework import serializers
from .models import *

class BoardGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardGame
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'data': {
                'id': representation['id'],
                'type': 'boardgames',
                'attributes': {
                    'title': representation['title'],
                    'cover_image': representation['cover_image'],
                    'min_players': representation['min_players'],
                    'max_players': representation['max_players'],
                    'min_playtime': representation['min_playtime'],
                    'max_playtime': representation['max_playtime'],
                    'categories': representation['categories'],
                    'cooperative': representation['cooperative'],
                    'description': representation['description'],
                    'year_published': representation['year_published'],
                    'rating': representation['rating'],
                    'rank': representation['rank'],
                    'abstracts_rank': representation['abstracts_rank'],
                    'cgs_rank': representation['cgs_rank'],
                    'childrens_games_rank': representation['childrens_games_rank'],
                    'family_games_rank': representation['family_games_rank'],
                    'party_games_rank': representation['party_games_rank'],
                    'strategy_games_rank': representation['strategy_games_rank'],
                    'thematic_rank': representation['thematic_rank'],
                    'wargames_rank': representation['wargames_rank'],
                },
            }
        }