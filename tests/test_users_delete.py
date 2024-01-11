import allure
import requests
from allure_commons.types import Severity
from utils.log_extending import step
from utils.allure_attach import response_logging, response_attaching


@step
def test_correct_execution(get_base_api_url, create_test_user):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Удаление пользователя")

    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/{create_test_user}"

    # ACTIONS (WHEN)
    response = requests.delete(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 204


@step
def test_execution_with_unknown_id(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Удаление не известного пользователя")

    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/unknown_id"

    # ACTIONS (WHEN)
    response = requests.delete(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 204
