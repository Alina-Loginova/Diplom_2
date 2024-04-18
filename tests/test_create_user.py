import requests
import allure

from urls import REGISTER

@allure.suite('Регистрация пользователя')
class TestCreateUser:
    @allure.title('Успешная регистрация нового пользователя')
    def test_create_new_user(self, register_new_user):
        assert register_new_user['response'].status_code == 200 and register_new_user['response'].json().get('success') == True

    @allure.title('Повторная регистрация пользователя')
    def test_create_used_user(self, register_new_user):
        payload = {
            "email": register_new_user['login_pass']['email'],
            "password": register_new_user['login_pass']['password'],
            "name": register_new_user['login_pass']['name']
        }
        response = requests.post(REGISTER, data=payload)
        assert response.status_code == 403 and response.json().get('message')== "User already exists"

    @allure.title('Регистрация курьера без обязательных атрибутов')
    def test_create_user_without_required_attr(self, generate_payload):
        payload = generate_payload
        del payload['email']
        response = requests.post(REGISTER, data=payload)
        assert response.status_code == 403 and response.json().get('message')== "Email, password and name are required fields"