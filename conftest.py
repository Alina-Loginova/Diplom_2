import requests
import pytest

from helpers import generate_random_string
from urls import REGISTER, INGREDIENTS, ORDERS


@pytest.fixture 
def register_new_user():
    login_pass = []
    email = generate_random_string(10) + '@gmail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(REGISTER, data=payload)
    if response.status_code == 200:
        login_pass = {
        "email": email,
        "password": password,
        "name": name
    }
    return {'login_pass': login_pass, 'response': response}

@pytest.fixture 
def generate_payload():
    email = generate_random_string(10) + '@gmail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    yield payload

@pytest.fixture 
def get_ingredients():
    response = requests.get(INGREDIENTS)
    return response.json().get('data')

@pytest.fixture 
def create_order(register_new_user, get_ingredients):
    payload = {
        "ingredients": [
            get_ingredients[0].get('_id'),
            get_ingredients[1].get('_id')
        ]   
    }
    headers = {
        'Authorization': register_new_user['response'].json().get('accessToken')
        }
    response = requests.post(ORDERS, headers=headers, data=payload)
    return {'headers': headers, 'response': response}