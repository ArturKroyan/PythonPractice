import csv
import json
import sys
from pathlib import Path


# Пути к файлам
BASE_DIR = Path(__file__).parent
DAY03_DIR = BASE_DIR.parent / "day03"

JSON_FILE = BASE_DIR / "students.json"
CSV_FILE = BASE_DIR / "students.csv"

REPORTS_DIR = BASE_DIR / "reports"
REPORT_FILE = REPORTS_DIR / "report.txt"


# Получаем список студентов из третьего дня
sys.path.append(str(DAY03_DIR))
from students import students


# Сохранение студентов в JSON
def save_to_json(students):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# Сохранение студентов в CSV
def save_to_csv(students):
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["name", "age", "group", "grades"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            row = student.copy()
            row["grades"] = ",".join(map(str, student["grades"]))
            writer.writerow(row)


# Чтение студентов из JSON
def load_from_json():
    if not JSON_FILE.exists():
        print("JSON-файл не найден.")
        return []

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Чтение студентов из CSV
def load_from_csv():
    if not CSV_FILE.exists():
        print("CSV-файл не найден.")
        return []

    students_from_csv = []

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["age"] = int(row["age"])
            row["grades"] = [int(grade) for grade in row["grades"].split(",")]
            students_from_csv.append(row)

    return students_from_csv


# Импорт из CSV с пропуском некорректных строк
def import_students_from_csv():
    if not CSV_FILE.exists():
        print("CSV-файл не найден.")
        return []

    imported_students = []

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                student = {
                    "name": row["name"].strip(),
                    "age": int(row["age"]),
                    "group": row["group"].strip(),
                    "grades": [
                        int(grade)
                        for grade in row["grades"].split(",")
                    ]
                }

                if not student["name"] or not student["group"]:
                    continue

                imported_students.append(student)

            except (ValueError, KeyError, AttributeError):
                continue

    return imported_students


# Формирование текстового отчёта
def create_report(students):
    REPORTS_DIR.mkdir(exist_ok=True)

    if not students:
        text = "Нет данных для формирования отчёта."

    else:
        average_age = (
            sum(student["age"] for student in students)
            / len(students)
        )

        all_grades = [
            grade
            for student in students
            for grade in student["grades"]
        ]

        average_grade = sum(all_grades) / len(all_grades)

        groups = sorted({
            student["group"]
            for student in students
        })

        text = (
            "=== ОТЧЁТ ПО СТУДЕНТАМ ===\n\n"
            f"Количество студентов: {len(students)}\n"
            f"Средний возраст: {average_age:.2f}\n"
            f"Средний балл: {average_grade:.2f}\n"
            f"Минимальная оценка: {min(all_grades)}\n"
            f"Максимальная оценка: {max(all_grades)}\n"
            f"Уникальные группы: {', '.join(groups)}\n"
        )

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write(text)


# Основная часть программы
save_to_json(students)
save_to_csv(students)

print("Студенты сохранены в JSON и CSV.")

json_students = load_from_json()
csv_students = load_from_csv()

print(f"Количество студентов в JSON: {len(json_students)}")
print(f"Количество студентов в CSV: {len(csv_students)}")

imported_students = import_students_from_csv()

print(
    f"Корректно импортировано студентов из CSV: "
    f"{len(imported_students)}"
)

create_report(imported_students)

print("Отчёт сохранён в reports/report.txt")