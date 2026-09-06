from collections import Counter


students = [
    {"name": "Артур", "age": 23, "group": "ИП-123", "grades": [5, 4, 5, 4, 5]},
    {"name": "Анна", "age": 19, "group": "ИП-123", "grades": [5, 5, 4, 5, 5]},
    {"name": "Максим", "age": 20, "group": "ИП-124", "grades": [3, 4, 4, 5, 3]},
    {"name": "Елена", "age": 21, "group": "ИП-125", "grades": [5, 5, 5, 4, 5]},
    {"name": "Иван", "age": 18, "group": "ИП-124", "grades": [3, 3, 4, 3, 4]},
    {"name": "Мария", "age": 20, "group": "ИП-123", "grades": [4, 5, 5, 4, 5]},
    {"name": "Дмитрий", "age": 22, "group": "ИП-125", "grades": [4, 4, 3, 5, 4]},
    {"name": "Ольга", "age": 19, "group": "ИП-124", "grades": [5, 4, 4, 5, 4]},
    {"name": "Алексей", "age": 21, "group": "ИП-123", "grades": [3, 4, 5, 4, 4]},
    {"name": "София", "age": 18, "group": "ИП-125", "grades": [5, 5, 5, 5, 4]},
    {"name": "Никита", "age": 20, "group": "ИП-124", "grades": [4, 3, 4, 4, 5]},
    {"name": "Анна", "age": 22, "group": "ИП-125", "grades": [4, 5, 4, 5, 5]},
    {"name": "Сергей", "age": 19, "group": "ИП-123", "grades": [3, 3, 4, 4, 3]},
    {"name": "Иван", "age": 21, "group": "ИП-125", "grades": [5, 4, 5, 4, 4]},
    {"name": "Виктория", "age": 20, "group": "ИП-124", "grades": [5, 5, 4, 5, 4]}
]


def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])


def get_top_students(students):
    return sorted(students, key=average_grade, reverse=True)[:5]


def filter_by_group(students, group):
    return [student for student in students if student["group"] == group]


def sort_by_age(students):
    return sorted(students, key=lambda student: student["age"])


def sort_by_average_grade(students):
    return sorted(students, key=average_grade, reverse=True)


def find_duplicate_names(students):
    names = [student["name"] for student in students]
    name_counts = Counter(names)

    return [name for name, count in name_counts.items() if count > 1]


def get_unique_groups(students):
    return {student["group"] for student in students}


def create_report(students):
    report = "=== ОТЧЁТ ПО СТУДЕНТАМ ===\n\n"

    report += "Все студенты:\n"
    for student in students:
        report += (
            f'{student["name"]}, '
            f'возраст: {student["age"]}, '
            f'группа: {student["group"]}, '
            f'средний балл: {average_grade(student):.2f}\n'
        )

    report += "\nТоп-5 студентов:\n"
    for student in get_top_students(students):
        report += f'{student["name"]}: {average_grade(student):.2f}\n'

    report += "\nПовторяющиеся имена:\n"
    report += ", ".join(find_duplicate_names(students))

    report += "\n\nУникальные группы:\n"
    report += ", ".join(sorted(get_unique_groups(students)))

    return report




if __name__ == "__main__":
    print(create_report(students))

    print("\n=== СТУДЕНТЫ ГРУППЫ ИП-123 ===")
    for student in filter_by_group(students, "ИП-123"):
        print(student["name"])

    print("\n=== СОРТИРОВКА ПО ВОЗРАСТУ ===")
    for student in sort_by_age(students):
        print(f'{student["name"]}: {student["age"]}')

    print("\n=== СОРТИРОВКА ПО СРЕДНЕМУ БАЛЛУ ===")
    for student in sort_by_average_grade(students):
        print(f'{student["name"]}: {average_grade(student):.2f}')