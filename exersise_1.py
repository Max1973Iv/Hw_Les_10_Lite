# Создать функцию convert_to_int(value), которая пытается преобразовать строку в целое число. Обработать случаи,
# когда преобразование невозможно, и когда возникает любое другое исключение.
import sys
import io
#
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Ошибка: Невозможно преобразовать строку в целое число."
    except Exception as e:
        return f"Произошло исключение: {e}"
    finally:
        print("Завершение попытки преобразования.")
# Пример использования функции
print(convert_to_int("123"))  # Вывод: 123
print(convert_to_int("abc"))  # Вывод: Ошибка: Невозможно преобразовать строку в целое число.
print(convert_to_int([1,2,3]))   # Вывод: Произошло исключение: ... (в зависимости от ошибки)