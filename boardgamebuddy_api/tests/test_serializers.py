from django.test import TestCase
from boardgamebuddy_api.models import User, UserBoardGame
from boardgamebuddy_api.popos import BoardGame
from boardgamebuddy_api.serializers import UserBoardGameSerializer, BoardGameSerializer, UserSerializer


class SerializersTest(TestCase):
    def test_user_board_game_serializer(self):
        user = User.objects.create(name="John Doe", email="john@example.com", image_path="example.jpg")
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
                'image_path': '/path/to/image.jpg',
                'rank': 'A',
            }
        }

        board_game = BoardGame(board_game_data)
        serializer = BoardGameSerializer(board_game)

        expected_data = {
            'id': '1',
            'title': 'Game 1',
            'image_path': '/path/to/image.jpg',
            'rank': 'A',
        }

        self.assertEqual(serializer.data, expected_data)

    def test_user_serializer(self):
        user = User.objects.create(name="John Doe", email="john@example.com", image_path="example.jpg")
        serializer = UserSerializer(user)

        expected_data = {
            'data': {
                'id': '1',
                'type': 'user',
                'attributes': {
                    'name': 'John Doe',  # Correct the expected 'name' value here
                    'email': 'john@example.com',
                    'image_path': '/path/to/image.jpg',
                },
            }
        }

        self.assertEqual(serializer.data, expected_data)


if __name__ == '__main__':
    unittest.main()