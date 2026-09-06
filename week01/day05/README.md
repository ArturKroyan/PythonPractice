# День 5 — Модули, пакеты, docstring и тесты

## Что выполнено

- Создан Python-пакет `student_tools`.
- Функции анализа студентов вынесены в `analysis.py`.
- Функция проверки возраста вынесена в `validation.py`.
- Для функций добавлены docstring.
- Добавлены автоматические тесты с использованием pytest.
- Реализована параметризация тестов.
- Выполняется 13 тестов.
- Добавлен `requirements.txt`.

## Установка зависимостей

Из корня проекта:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Перейти в папку пятого дня:

```bash
cd week01/day05
```

Запустить тесты:

```bash
pytest -v
```

Ожидаемый результат:

```text
13 passed
```

## Структура

```text
day05/
├── student_tools/
│   ├── __init__.py
│   ├── analysis.py
│   └── validation.py
├── tests/
│   └── test_student_tools.py
└── README.md
```