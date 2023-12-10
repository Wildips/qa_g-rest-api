import jsonschema as jsonschema
import allure
import requests
import json
from allure_commons.types import Severity

from utils.resource import load_schema


def test_correct_execution(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки register")

    allure.dynamic.story("Создание пользователя")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}register"
    test_schema = load_schema("register_endpoint/post_method/register.json")
    body = json.loads('{"email": "eve.holt@reqres.in", "password": "pistol"}')

    # ACTIONS (WHEN)
    response = requests.post(test_url, data=body)

    # ASSERT (THEN)
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=test_schema)


def test_execution_with_incorrect_body_data(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки register")

    allure.dynamic.story(
        "Создание пользователя с не верным пользователем в теле запроса"
    )
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}register"
    body = json.loads('{"email": "some@mail.io", "password": "some_password"}')

    # ACTIONS (WHEN)
    response = requests.post(test_url, data=body)

    # ASSERT (THEN)
    assert response.status_code == 400
    assert response.text == '{"error":"Note: Only defined users succeed registration"}'
