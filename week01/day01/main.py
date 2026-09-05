name = "Артур"
group = "ИП-123"
age = 23
interests = "Прогр, тестирование ПО"
print("===Визитка===")
print(f"Имя:{name}")
print(f"Группа:{group}")
print(f"Возраст:{age}")
print(f"Интересы:{interests}")

print("\n=== Преобразование температуры ===")

celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"Температура по Фаренгейту: {fahrenheit}")



print("\n=== Расчёт стоимости со скидкой ===")

price = float(input("Введите стоимость покупки: "))
discount = float(input("Введите скидку в процентах: "))

final_price = price - price * discount / 100

print(f"Итоговая стоимость: {final_price}")


print("\n=== Нормализация имени ===")

user_name = input("Введите имя: ")
normalized_name = user_name.strip().capitalize()

print(f"Нормализованное имя: {normalized_name}")