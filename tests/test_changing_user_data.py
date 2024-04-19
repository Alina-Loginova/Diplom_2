import requests
import allure

from urls import USER_DATA

@allure.suite('Авторизация юзера')
class TestChangingUserData:
    @allure.title('Успешная изменение данных пользователя')
    def test_changing_user_data(self, register_new_user):
        payload = {
            "email": register_new_user['login_pass']['email'] + '1',
            "password": register_new_user['login_pass']['password'] + '1',
            "name": register_new_user['login_pass']['name'] + '1'
        }
        headers = {
            'Authorization': register_new_user['response'].json().get('accessToken')
            }
        response = requests.patch(USER_DATA, headers=headers, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Изменение данных пользователя без токена')
    def test_changing_user_data_without_token(self, register_new_user):
        payload = {
            "email": register_new_user['login_pass']['email'] + '1',
            "password": register_new_user['login_pass']['password'] + '1',
            "name": register_new_user['login_pass']['name'] + '1'
        }
        response = requests.patch(USER_DATA, data=payload)
        assert response.status_code == 401 and response.json().get('message')== "You should be authorised"