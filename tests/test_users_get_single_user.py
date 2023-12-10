import jsonschema as jsonschema
import allure
import requests
from allure_commons.types import Severity

from utils.resource import load_schema

USER_ID = 2


def test_correct_execution(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение данных пользователя по id")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/{USER_ID}"
    test_schema = load_schema("users_endpoint/get_method/single_user.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)

    # ASSERT (THEN)
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=test_schema)


def test_execution_with_unknown_id_in_url(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение данных несуществующего пользователя по id")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/unknown_id"

    # ACTIONS (WHEN)
    response = requests.get(test_url)

    # ASSERT (THEN)
    assert response.status_code == 404
    assert response.text == "{}"
