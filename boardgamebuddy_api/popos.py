class BoardGame:
	def __init__(self, data):
		self.id = data['id']
		self.title = data['attributes']['title']
		self.image_path = data['attributes']['image_path']
		self.rank = data['attributes']['rank']