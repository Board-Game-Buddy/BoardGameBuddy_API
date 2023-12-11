from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient
from boardgamebuddy_api.models import User, UserBoardGame

class ViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(name="User", email="user@test.com", image_path="test/path")
        self.user1_board_game = UserBoardGame.objects.create(user=self.user1, board_game_id=2)

        self.user2 = User.objects.create(name="User2", email="user2@test.com", image_path="test/path")

    def test_users_list_get(self):
        url = '/users/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertEqual(len(data), 2)
        user_data = data[0]['data']

        self.assertEqual(user_data['id'], self.user1.id)
        self.assertEqual(user_data['attributes']['name'], self.user1.name)
        self.assertEqual(user_data['attributes']['email'], self.user1.email)
        self.assertEqual(user_data['attributes']['image_path'], self.user1.image_path)
        self.assertEqual(user_data['type'], 'user')

    def test_user_details_get(self):
        url = '/users/1'
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = response.json()['data']


        expected_user_data = {
            'id': 1,
            'attributes': {
                'name': 'User',
                'email': 'user@test.com',
                'image_path': 'test/path',
            },
            'type': 'user'
        }

        self.assertEqual(user_data, expected_user_data)

    def test_user_list_post(self):
            url = '/users/'

            new_user_data = {
                'name': 'User3',
                'email': 'user3@test.com',
                'image_path': 'test/path',
            }

            response = self.client.post(url, data=new_user_data, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            new_user_attributes = response.json().get('data', {}).get('attributes', {})

            self.assertEqual(new_user_attributes.get('name'), new_user_data.get('name'))
            self.assertEqual(new_user_attributes.get('email'), new_user_data.get('email'))
            self.assertEqual(new_user_attributes.get('image_path'), new_user_data.get('image_path'))

    def test_user_list_post_sad(self):
        url = '/users/'

        new_user_data = {
            'name': 'User4',
        }

        response = self.client.post(url, data=new_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_details_get_not_found(self):
        url = '/users/5'
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'User not found')

    def test_user_details_patch(self):
        url = '/users/2'

        self.assertTrue(User.objects.filter(pk=self.user2.id).exists())

        data = {
            'name': 'UpdatedName',
            'email': 'updatedemail@test.com',
            'image_path': 'updated/test/path'
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = response.json()

        self.assertEqual(user_data['data']['id'], self.user2.id)
        self.assertEqual(user_data['data']['attributes']['name'], 'UpdatedName')
        self.assertEqual(user_data['data']['attributes']['email'], 'updatedemail@test.com')
        self.assertEqual(user_data['data']['attributes']['image_path'], 'updated/test/path')

    def test_user_details_patch_sad(self):
        url = '/users/2'
        invalid_data = {'email': 'invalid_email'}
        response = self.client.patch(url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_details_delete(self):
        url = '/users/2'

        self.assertTrue(User.objects.filter(pk=self.user2.id).exists())

        response = self.client.delete(url)

        expected_response = Response("User Deleted", status=status.HTTP_204_NO_CONTENT).data
        self.assertEqual(response.data, expected_response)
        self.assertFalse(User.objects.filter(pk=self.user2.id).exists())

    def test_user_boardgames_get(self):
        url = '/users/1/favorites'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        board_game = response.json()[0]

        self.assertEqual(board_game['id'], "2")
        self.assertEqual(board_game['title'], "Pandemic Legacy: Season 1")
        self.assertEqual(board_game['image_path'], "https://cf.geekdo-images.com/-Qer2BBPG7qGGDu6KcVDIw__original/img/PlzAH7swN1nsFxOXbfUvE3TkE5w=/0x0/filters:format(png)/pic2452831.png")
        self.assertEqual(board_game['rank'], "2")

    def test_user_boardgames_post(self):
        url = '/users/1/favorites?board_game_id=3'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_boardgames_post_sad(self):
        url = '/users/1/favorites?board_game_id=invalid_id'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_boardgames_delete(self):
            url = '/users/1/favorites?board_game_id=3'
            response = self.client.delete(url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            expected_response = Response("User Favorite Deleted", status=status.HTTP_204_NO_CONTENT).data
            self.assertEqual(response.data, expected_response)

if __name__ == '__main__':
    unittest.main()