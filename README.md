# Проект по API тестированию

> <a target="_blank" href="https://reqres.in/">reqres.in</a>

![This is an image](/images/test_page.png)

#### Список проверок, реализованных в авто-тестах

- [x] Регистрация пользователя (POST)
- [x] Удаление пользователя (DELETE)
- [x] Получение списка пользователей (GET)
- [x] Получение пользователя по id (GET)
- [x] Создание пользователя по id (POST)
- [x] Обновление данных пользователя (UPDATE)

#### Параметры сборки

* `ENVIRONMENT` - параметр определяет окружение для запуска тестов, по умолчанию STAGE
* `COMMENT` - комментарий к сборке

### Для запуска авто-тестов в Jenkins

#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_g_diplome/">проект</a>

![This is an image](/images/jenfins_project_main.png)

#### 2. Выбрать пункт **Build with Parameters**

#### 3. Внести изменения в конфигурации сборки, при необходимости

#### 4. Нажать **Build**

#### 5. Результат запуска сборки можно посмотреть как в классическом формате Allure Results

![This is an image](/images/allure_example.png)

#### 6. Так и в интегрированном с Jira и Allure TestOps

![This is an image](/images/testops_example.png)

#### 7. Информация о завершении сборки так же будет опубликована в telegram на канале

![This is an image](/images/notiffication_example.png)

## Запуск авто-тестов

Пример командной строки:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -vv -s .
```

Создание локального отчета:

```bash
allure serve allure-results
```

:heart: <a target="_blank" href="https://qa.guru">qa.guru</a><br/>
