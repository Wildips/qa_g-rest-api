import allure
import requests
import json
from allure_commons.types import Severity
import jsonschema as jsonschema
from utils.resource import load_schema
from utils.log_extending import step
from utils.allure_attach import response_logging, response_attaching


@step
def test_correct_execution(get_base_api_url, create_test_user):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Обновление данных пользователя")

    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/{create_test_user}"
    test_schema = load_schema("users_endpoint/put_method/update.json")
    body = json.loads('{"name": "kotofeus", "job": "watcher"}')

    # ACTIONS (WHEN)
    response = requests.put(test_url, data=body)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["name"] == "kotofeus"
    assert response.json()["job"] == "watcher"
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_execution_for_incorrect_user(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Обновление данных не существующего пользователя")

    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/some_id"
    test_schema = load_schema("users_endpoint/put_method/update.json")
    body = json.loads('{"name": "kotofeus", "job": "watcher"}')

    # ACTIONS (WHEN)
    response = requests.put(test_url, data=body)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["name"] == "kotofeus"
    assert response.json()["job"] == "watcher"
    jsonschema.validate(instance=response.json(), schema=test_schema)
