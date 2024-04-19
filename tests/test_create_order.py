import requests
import allure

from urls import ORDERS

@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('Успешное создание заказа с токеном')
    def test_create_order_with_auth(self, register_new_user, get_ingredients):
        payload = {
            "ingredients": [
                get_ingredients[0].get('_id')
            ]   
        }
        headers = {
            'Authorization': register_new_user['response'].json().get('accessToken')
            }
        response = requests.post(ORDERS, headers=headers, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Успешное создание заказа без токена')
    def test_create_order_without_auth(self, get_ingredients):
        payload = {
            "ingredients": [
                get_ingredients[0].get('_id'),
                get_ingredients[1].get('_id'),
            ]   
        }
        response = requests.post(ORDERS, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, register_new_user, get_ingredients):
        payload = {
            "ingredients": []   
        }
        headers = {
            'Authorization': register_new_user['response'].json().get('accessToken')
            }
        response = requests.post(ORDERS, headers=headers, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "Ingredient ids must be provided"

    @allure.title('Создание заказа с невалидным хешом')
    def test_create_order_with_invalid_hash(self, register_new_user, get_ingredients):
        payload = {
            "ingredients": [
                "61c0c3d71d1f82001bdaaa6d"
            ]   
        }
        headers = {
            'Authorization': register_new_user['response'].json().get('accessToken')
            }
        response = requests.post(ORDERS, headers=headers, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "One or more ids provided are incorrect"