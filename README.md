# qa-guru-homework-20

Мобильная автоматизация тестов на **Appium** для Android-приложения Wikipedia Alpha. Проект использует **Selene**, **Pydantic Settings** и **Allure**.

## Стек

- Python 3.9+
- [Appium](https://appium.io/) (UiAutomator2)
- [Selene](https://github.com/yashaka/selene) — обёртка над Selenium
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) — конфигурация из переменных окружения
- [pytest](https://pytest.org/) + [Allure](https://allure.qatools.ru/)

## Установка

```bash
poetry install
```

## Подготовка окружения

1. **APK-файл** приложения положите в каталог `apps/`:
   - `apps/app-alpha-universal-release.apk`

2. **Переменные окружения** задаются через `.env` и контекстный файл `.env.{CONTEXT}`.

   В корне создайте `.env` с обязательной переменной:

   ```env
   CONTEXT=local_emulator
   ```

   Отредактируйте файл конфигурации для выбранного контекста, например `.env.local_emulator`:

   ```env
   REMOTE_URL=http://127.0.0.1:4723
   PLATFORM_NAME=Android
   PLATFORM_VERSION=13.0
   DEVICE_NAME=emulator-5554
   app=./apps/app-alpha-universal-release.apk
   AUTOMATION_NAME=UiAutomator2
   ```


3. **Appium Server** должен быть запущен и доступен по `REMOTE_URL` (для эмулятора обычно `http://127.0.0.1:4723`).

## Запуск тестов

```bash
# Все тесты
poetry run pytest tests/

# С отчётом Allure
poetry run pytest tests/ --alluredir=allure-results

# Просмотр отчёта Allure (после генерации)
allure serve allure-results
```

Через скрипты из `pyproject.toml`:

```bash
poetry run test
poetry run test-with-allure
```

## Структура проекта

```
├── apps/                    # APK приложения
├── tests/
│   ├── conftest.py          # фикстуры (драйвер, Allure, скриншоты)
│   └── test_wikipedia_android.py
├── utils/                   # вспомогательные функции
├── config.py                # конфигурация на Pydantic Settings
├── .env                     # CONTEXT и общие переменные
├── .env.local_emulator      # настройки для эмулятора
└── .env.local_real          # настройки для реального устройства
```

## Линтеры и типы

```bash
poetry run black .
poetry run flake8 .
poetry run mypy config.py config3.py utils/ tests/
```

