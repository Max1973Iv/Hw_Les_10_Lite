#Создать функцию validate_user_input(data), которая принимает словарь с данными пользователя.
# Функция должна проверять наличие и корректность ключей name (строка) и age (положительное число).
# В случае некорректных данных генерировать соответствующие исключения.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#
def validate_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("аргумент должен быть словарём")
    try:
        if 'name' not in data :# ключ name нет в словаре
            raise ValueError("отсутствует ключ 'name'")
        if not isinstance(data['name'], str):# ключ name не строка
            raise TypeError("ключ 'name'не строка")
        if 'age' not in data :# ключа age нет в словаре
            raise ValueError("отсутствует ключ 'age'")
        if not isinstance(data['age'], int) or data['age'] <= 0:# ключ age не положительное число
            raise ValueError("ключ 'age' не положительное число")
    except ValueError as dict_error:
        raise ValueError(f'Ошибка ключей словаря {dict_error}') from dict_error
    return True
# Пример использования функции
try:
    user_data = {'name': 'Alice', 'age': 30}
    print(validate_user_input(user_data))  # Вывод: True    корректные данные
except Exception as e:
    print(f"Ошибка: {e}")
try:
    missing_name_data = {'age': 25}
    print(validate_user_input(missing_name_data))  # отсутствует имя
except Exception as e:
    print(f"Ошибка: {e}")
try:
    invalid_data = {'name': 'Bob', 'age': -5}
    print(validate_user_input(invalid_data))  # неверный возраст
except Exception as e:
    print(f"Ошибка: {e}")
try:
    non_dict_data = ['name', 'Charlie', 'age', 25]
    print(validate_user_input(non_dict_data))  # не словарь
except Exception as e:
    print(f"Ошибка: {e}")