def validate_age(value):
    try:
        age = int(value)

        if 0 <= age <= 120:
            return True
        else:
            return False

    except ValueError:
        return False


value = input("Введите возраст: ")

if validate_age(value):
    print("Возраст введён корректно")
else:
    print("Некорректный возраст")