from .services import BoardGamesService
from .popos import BoardGame

class BoardGamesFacade:
	def __init__(self, board_game_ids):
		self.board_games_service = BoardGamesService()
		self.board_game_ids = board_game_ids

	def get_board_game_data(self):
		board_games_data = self.board_games_service.get_board_games(self.board_game_ids)
		board_games = [BoardGame(game) for game in board_games_data]
		return board_games