from collections import Counter


def average_grade(student):
    """Вычисляет средний балл студента."""
    return sum(student["grades"]) / len(student["grades"])


def get_top_students(students):
    """Возвращает пять студентов с наибольшим средним баллом."""
    return sorted(students, key=average_grade, reverse=True)[:5]


def filter_by_group(students, group):
    """Возвращает студентов указанной группы."""
    return [
        student
        for student in students
        if student["group"] == group
    ]


def sort_by_age(students):
    """Возвращает студентов, отсортированных по возрасту."""
    return sorted(students, key=lambda student: student["age"])


def sort_by_average_grade(students):
    """Возвращает студентов по убыванию среднего балла."""
    return sorted(students, key=average_grade, reverse=True)


def find_duplicate_names(students):
    """Возвращает повторяющиеся имена студентов."""
    names = [student["name"] for student in students]
    name_counts = Counter(names)

    return [
        name
        for name, count in name_counts.items()
        if count > 1
    ]


def get_unique_groups(students):
    """Возвращает множество уникальных групп."""
    return {student["group"] for student in students}