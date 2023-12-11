from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from django.urls import path
from boardgamebuddy_api import views

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
			response = self.client.patch(url, format='json')

			self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

			response_data = response.json()

			self.assertEqual(response_data, "User Deleted")