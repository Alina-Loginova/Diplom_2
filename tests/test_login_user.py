import requests
import allure

from urls import LOGIN

@allure.suite('Авторизация юзера')
class TestLoginUser:
    @allure.title('Успешная авторизация юзера')
    def test_login_user(self, register_new_user):
        payload = {
            "email": register_new_user['login_pass']['email'],
            "password": register_new_user['login_pass']['password']
        }
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Авторизация с невалидным паролем и логином пользователя')
    def test_login_user_with_invalid_password_and_email(self, register_new_user):
        payload = {
            "email": register_new_user['login_pass']['email'] + '1',
            "password": register_new_user['login_pass']['password'] + '1'
        }
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 401 and response.json().get('message')== "email or password are incorrect"