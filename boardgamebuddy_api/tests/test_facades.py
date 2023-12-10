import unittest
from unittest.mock import MagicMock
from boardgamebuddy_api.facades import BoardGamesFacade

class BoardGamesFacadeTest(unittest.TestCase):
    def setUp(self):
        self.board_games_service_mock = MagicMock()
        self.board_games_service_mock.get_board_games.return_value = [
            {"id": 1, "attributes": {"title": "Game 1", "image_path": "/path/to/game1.jpg", "rank": 1}},
            {"id": 2, "attributes": {"title": "Game 2", "image_path": "/path/to/game2.jpg", "rank": 2}},
        ]
        
        self.facades = BoardGamesFacade([1, 2])
        self.facades.board_games_service = self.board_games_service_mock

    def test_get_board_game_data(self):
        result = self.facades.get_board_game_data()

        self.board_games_service_mock.get_board_games.assert_called_once_with([1, 2])

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].title, "Game 1")
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].title, "Game 2")

if __name__ == '__main__':
    unittest.main()