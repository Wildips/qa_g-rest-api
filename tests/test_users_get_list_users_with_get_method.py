import allure
import requests
import pytest
import jsonschema as jsonschema
from allure_commons.types import Severity
from qa_g_rest_api_tests.utils.resource import load_schema
from qa_g_rest_api_tests.utils.log_extending import step
from qa_g_rest_api_tests.utils.allure_attach import response_logging, response_attaching


@step
@pytest.mark.parametrize("id_", [1, 2])
def test_correct_execution_for_page_(get_base_api_url, id_):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение списка пользователей")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/?page={id_}"
    test_schema = load_schema("users_endpoint/get_method/list_users.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["page"] == id_
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_execution_with_miss_print_url_return_first_page(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Возврат первой страницы при ошибке в параметре")
    # ARRANGE (GIVEN)
    page_id = 2
    test_url = f"{get_base_api_url}users/?pe={page_id}"
    test_schema = load_schema("users_endpoint/get_method/list_users.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["page"] == 1
    jsonschema.validate(instance=response.json(), schema=test_schema)


def test_execution_with_huge_page(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Возврат пустой страницы при большом значении параметра")
    # ARRANGE (GIVEN)
    page_id = 9999999
    test_url = f"{get_base_api_url}users/?page={page_id}"
    test_schema = load_schema(
        "users_endpoint/get_method/huge_page_value_list_users.json"
    )

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["page"] == page_id
    jsonschema.validate(instance=response.json(), schema=test_schema)
