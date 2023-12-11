from django.test import TestCase
from boardgamebuddy_api.models import User, UserBoardGame
from boardgamebuddy_api.popos import BoardGame
from boardgamebuddy_api.serializers import UserBoardGameSerializer, BoardGameSerializer, UserSerializer


class SerializersTest(TestCase):
    def test_user_board_game_serializer(self):
        user = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        user_board_game = UserBoardGame.objects.create(user=user, board_game_id=123)

        serializer = UserBoardGameSerializer(user_board_game)

        expected_data = {
            'id': 1,
            'user': 1,
            'board_game_id': 123,
        }

        self.assertEqual(serializer.data, expected_data)

    def test_board_game_serializer(self):
        board_game_data = {
            'id': 1,
            'attributes': {
                'title': 'Game 1',
                'image_path': 'test/path',
                'rank': '12',
            }
        }

        board_game = BoardGame(board_game_data)
        serializer = BoardGameSerializer(board_game)

        expected_data = {
            'id': '1',
            'title': 'Game 1',
            'image_path': 'test/path',
            'rank': '12',
        }

        self.assertEqual(serializer.data, expected_data)

    def test_user_serializer(self):
        user = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        serializer = UserSerializer(user)

        expected_data = {
            'data': {
                'id': 1,
                'type': 'user',
                'attributes': {
                    'name': 'User',
                    'email': 'user@test.com',
                    'image_path': 'test/path',
                },
            }
        }

        self.assertEqual(serializer.data, expected_data)


if __name__ == '__main__':
    unittest.main()