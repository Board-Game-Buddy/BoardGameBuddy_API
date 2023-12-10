import pytest
from django.conf import settings
from django.test import RequestFactory
from django.db import IntegrityError
from boardgamebuddy_api.models import User, UserBoardGame

@pytest.fixture
def sample_user():
    return User.objects.create(name='John Doe', email='john@example.com')

@pytest.fixture
def sample_user_board_game(sample_user):
    return UserBoardGame.objects.create(user=sample_user, board_game_id=123)

def test_user_model():
    user = User.objects.create(name='Test User', email='test@example.com', image_path='test.jpg')
    assert str(user) == 'Test User'

def test_user_board_game_model(sample_user_board_game):
    user_board_game = sample_user_board_game
    assert str(user_board_game) == f"{user_board_game.user.name}'s Favorite - BGID {user_board_game.board_game_id}"

def test_user_board_game_unique_constraint(sample_user):
    with pytest.raises(IntegrityError):
        UserBoardGame.objects.create(user=sample_user, board_game_id=123)