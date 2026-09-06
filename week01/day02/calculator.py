def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


while True:
    operation = input("Введите операцию (+, -, *, /) или exit для выхода: ")

    if operation == "exit":
        break

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = sub(a, b)
        elif operation == "*":
            result = mul(a, b)
        elif operation == "/":
            result = div(a, b)
        else:
            print("Неизвестная операция")
            continue

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: необходимо вводить числа")

    except ZeroDivisionError:
        print("Ошибка: делить на ноль нельзя")