from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, UserBoardGame

class UserListAPITest(APITestCase):
	def test_user_list_api_get(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')
		self.user2 = User.objects.create(name='testuser2', email='testuser2@example.com', image_path='testimage2')

		url = '/users'
		response = self.client.get(url, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)

		data = response.json()

		self.assertEqual(len(data), 2)
		self.assertEqual(data, [
			{
				"data": {
					"id": 1,
					"type": "user",
					"attributes": {
						"name": "testuser1",
						"email": "testuser1@example.com",
						"image_path": "testimage1"
					}
				}
			},
			{
				"data": {
					"id": 2,
					"type": "user",
					"attributes": {
						"name": "testuser2",
						"email": "testuser2@example.com",
						"image_path": "testimage2"
					}
				}
			}
		])

	def test_user_list_api_post(self):
		data = {
			"name": "testuser1",
			"email": "testuser1@example.com",
			"image_path": "testimage1"
		}
		url = '/users'
		response = self.client.post(url, data, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response_data = response.json()

		self.assertEqual(response_data, {
			"data": {
				"id": 1,
				"type": "user",
				"attributes": {
					"name": "testuser1",
					"email": "testuser1@example.com",
					"image_path": "testimage1"
				}
			}
		})

class UserDetailsAPITest(APITestCase):
	def test_user_details_api_get(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')

		url = '/users/1'
		response = self.client.get(url, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)

		data = response.json()

		self.assertEqual(data, {
			"data": {
				"id": 1,
				"type": "user",
				"attributes": {
					"name": "testuser1",
					"email": "testuser1@example.com",
					"image_path": "testimage1"
				}
			}
		})

	def test_user_details_api_patch(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')

		data = {
			"name": "testuser1_edit",
			"email": "testuser1@example.com",
			"image_path": "testimage1"
		}
		url = '/users/1'
		response = self.client.patch(url, data, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)

		response_data = response.json()

		self.assertEqual(response_data, {
			"data": {
				"id": 1,
				"type": "user",
				"attributes": {
					"name": "testuser1_edit",
					"email": "testuser1@example.com",
					"image_path": "testimage1"
				}
			}
		})

	def test_user_details_api_delete(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')

		url = '/users/1'
		response = self.client.delete(url, format='json')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

		with self.assertRaises(User.DoesNotExist):
    			self.user1.refresh_from_db()

class UserBoardGamesAPITest(APITestCase):
	def test_user_board_games_api_get(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')
		self.user_favorite_1 = UserBoardGame.objects.create(user=self.user1, board_game_id=1)

		url = '/users/1/favorites'
		response = self.client.get(url, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)

		data = response.json()

		self.assertEqual(data, [
			{
				"id": "1",
				"title": "Brass: Birmingham",
				"image_path": "https://cf.geekdo-images.com/x3zxjr-Vw5iU4yDPg70Jgw__original/img/FpyxH41Y6_ROoePAilPNEhXnzO8=/0x0/filters:format(jpeg)/pic3490053.jpg",
				"rank": "1"
			}
		])

	def test_user_board_games_api_post(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')

		url = '/users/1/favorites'
		url_with_query_param = f"{url}?board_game_id=1"
		response = self.client.post(url_with_query_param, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response_data = response.json()

		self.assertEqual(response_data, {
			"id": 1,
			"board_game_id": 1,
			"user": 1
		})

	def test_user_board_games_api_delete(self):
		self.user1 = User.objects.create(name='testuser1', email='testuser1@example.com', image_path='testimage1')
		self.user_favorite1 = UserBoardGame.objects.create(user=self.user1, board_game_id=1)

		url = '/users/1/favorites'
		url_with_query_param = f"{url}?board_game_id=1"
		response = self.client.delete(url_with_query_param, format='json')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

		with self.assertRaises(UserBoardGame.DoesNotExist):
    			self.user_favorite1.refresh_from_db()