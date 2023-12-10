import json
import allure
import pytest
import requests

BASE_API_URL = "https://reqres.in/api/"

@allure.title("Базовый URL API тестов : {BASE_API_URL}")
@pytest.fixture(scope="function")
def get_base_api_url():
    return BASE_API_URL


@allure.title("Создаем тестового пользователя")
@pytest.fixture(scope="function")
def create_test_user():
    test_url = f"{BASE_API_URL}users"
    body = json.loads('{"name": "morpheus1", "job": "leader_new"}')
    response = requests.post(test_url, data=body)
    return response.json()["id"]

