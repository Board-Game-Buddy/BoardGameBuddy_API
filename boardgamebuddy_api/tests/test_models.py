from django.test import TestCase
from boardgamebuddy_api.models import User, UserBoardGame

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        self.assertEqual(user.name, "User")
        self.assertEqual(user.email, "user@test.com")
        self.assertEqual(user.image_path, "test/path")

    def test_user_str(self):
        user = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        self.assertEqual(str(user), user.name)

class UserBoardGameModelTest(TestCase):
    def test_user_board_game_creation(self):
        user = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        user_board_game = UserBoardGame.objects.create(user=user, board_game_id=123)
        self.assertEqual(user_board_game.user, user)
        self.assertEqual(user_board_game.board_game_id, 123)

    def test_user_board_game_str(self):
        user = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        user_board_game = UserBoardGame.objects.create(user=user, board_game_id=123)
        expected_str = f"{user.name}'s Favorite - BGID {user_board_game.board_game_id}"
        self.assertEqual(str(user_board_game), expected_str)