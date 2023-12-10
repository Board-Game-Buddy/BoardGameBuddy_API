import unittest
from boardgamebuddy_api.popos import BoardGame

class BoardGameTest(unittest.TestCase):
    def test_board_game_initialization(self):
        data = {
            'id': 1,
            'attributes': {
                'title': 'Test Game',
                'image_path': '/path/to/image.jpg',
                'rank': 42,
            }
        }
        board_game = BoardGame(data)
        self.assertEqual(board_game.id, 1)
        self.assertEqual(board_game.title, 'Test Game')
        self.assertEqual(board_game.image_path, '/path/to/image.jpg')
        self.assertEqual(board_game.rank, 42)

if __name__ == '__main__':
    unittest.main()