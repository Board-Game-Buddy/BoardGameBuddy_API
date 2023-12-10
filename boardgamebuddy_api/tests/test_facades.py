from django.test import TestCase
from unittest.mock import MagicMock
from boardgamebuddy_api.facades import BoardGamesFacade

class BoardGamesFacadeTest(TestCase):
    def setUp(self):
        self.board_games_service_mock = MagicMock()
        self.board_games_service_mock.get_board_games.return_value = [
            {"id": 1, "name": "Game 1"},
            {"id": 2, "name": "Game 2"},
        ]

        self.facades = BoardGamesFacade([1, 2])
        self.facades.board_games_service = self.board_games_service_mock

    def test_get_board_game_data(self):
        result = self.facades.get_board_game_data()

        self.board_games_service_mock.get_board_games.assert_called_once_with([1, 2])

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, "Game 1")
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].name, "Game 2")