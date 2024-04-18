import requests
import allure

from urls import ORDERS

@allure.suite('Получение заказа')
class TestGetOrder:
    @allure.title('Успешное получение заказа с токеном')
    def test_get_order_with_auth(self, create_order):
        response = requests.get(ORDERS, headers=create_order['headers'])
        assert response.status_code == 200 and f'"number":{create_order['response'].json().get("order").get("number")}' in response.text

    @allure.title('Успешное получение заказа с токеном')
    def test_get_order_without_auth(self):
        response = requests.get(ORDERS)
        assert response.status_code == 401 and response.json().get('message') == 'You should be authorised'