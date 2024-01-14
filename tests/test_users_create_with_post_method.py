import allure
import requests
import json
import jsonschema as jsonschema
from allure_commons.types import Severity
from utils.resource import load_schema
from utils.log_extending import step
from utils.allure_attach import response_logging, response_attaching


@step
def test_correct_execution(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Создание пользователя")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users"
    test_schema = load_schema("users_endpoint/post_method/create.json")
    body = json.loads('{"name": "morpheus1", "job": "leader_new"}')

    # ACTIONS (WHEN)
    response = requests.post(test_url, data=body)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    assert response.json()["job"] == "leader_new"
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_execution_with_name_only(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Создание пользователя с одни параметром")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users"
    test_schema = load_schema("users_endpoint/post_method/create_with_name_only.json")
    body = json.loads('{"name": "morpheus1"}')

    # ACTIONS (WHEN)
    response = requests.post(test_url, data=body)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    jsonschema.validate(instance=response.json(), schema=test_schema)
