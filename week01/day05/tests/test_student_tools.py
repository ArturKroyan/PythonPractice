import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import pytest

from student_tools.analysis import (
    average_grade,
    get_top_students,
    filter_by_group,
    sort_by_age,
    sort_by_average_grade,
    find_duplicate_names,
    get_unique_groups,
)
from student_tools.validation import validate_age


students = [
    {"name": "Анна", "age": 19, "group": "ИП-123", "grades": [5, 5, 4]},
    {"name": "Иван", "age": 21, "group": "ИП-124", "grades": [3, 4, 4]},
    {"name": "Анна", "age": 22, "group": "ИП-125", "grades": [4, 5, 5]},
    {"name": "Олег", "age": 18, "group": "ИП-123", "grades": [5, 4, 4]},
    {"name": "Мария", "age": 20, "group": "ИП-124", "grades": [5, 5, 5]},
    {"name": "Павел", "age": 23, "group": "ИП-125", "grades": [3, 3, 4]},
]


def test_average_grade():
    student = {"grades": [5, 4, 3]}
    assert average_grade(student) == 4


def test_top_students_count():
    result = get_top_students(students)
    assert len(result) == 5


def test_top_students_first():
    result = get_top_students(students)
    assert result[0]["name"] == "Мария"


def test_filter_by_group():
    result = filter_by_group(students, "ИП-123")
    assert len(result) == 2


def test_sort_by_age():
    result = sort_by_age(students)
    assert result[0]["age"] == 18


def test_sort_by_average_grade():
    result = sort_by_average_grade(students)
    assert result[0]["name"] == "Мария"


def test_duplicate_names():
    result = find_duplicate_names(students)
    assert "Анна" in result


def test_unique_groups():
    result = get_unique_groups(students)
    assert result == {"ИП-123", "ИП-124", "ИП-125"}


@pytest.mark.parametrize(
    "value, expected",
    [
        ("23", True),
        ("0", True),
        ("120", True),
        ("121", False),
        ("abc", False),
    ],
)
def test_validate_age(value, expected):
    assert validate_age(value) == expected