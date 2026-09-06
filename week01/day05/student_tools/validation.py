def validate_age(value):
    """Проверяет, что возраст является числом от 0 до 120."""
    try:
        age = int(value)
        return 0 <= age <= 120
    except ValueError:
        return False