from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import User
from django.urls import path
from boardgamebuddy_api import views

class UserListAPITest(APITestCase, URLPatternsTestCase):
	urlpatterns = [
        path('users', views.user_list),
    ]

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