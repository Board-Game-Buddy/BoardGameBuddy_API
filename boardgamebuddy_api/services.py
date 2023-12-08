import requests

class BoardGamesService:
	def get_board_games(ids):
		url = "https://middleman-api-8d134831a182.herokuapp.com/api/v1/multi_board_games"
		# url = "http://127.0.0.1:3000/api/v1/multi_board_games"
		data = { 'ids': ids }
		headers = { 'Accepts': 'application/json' }

		response = requests.get(url, json=data, headers=headers)
		# import pdb; pdb.set_trace()

		return response.json().get('data', [])
		

# BoardGamesService.get_board_games()