from django.test import TestCase
from boardgamebuddy_api.models import User, UserBoardGame

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name="John Doe", email="john@example.com", image_path="example.jpg")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.image_path, "example.jpg")

class UserBoardGameModelTest(TestCase):
    def test_user_board_game_creation(self):
        user = User.objects.create(name="John Doe", email="john@example.com", image_path="example.jpg")
        user_board_game = UserBoardGame.objects.create(user=user, board_game_id=123)
        self.assertEqual(user_board_game.user, user)
        self.assertEqual(user_board_game.board_game_id, 123)