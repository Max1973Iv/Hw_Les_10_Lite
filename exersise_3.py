# Создать класс NegativeNumberError, который будет генерироваться, если переданное число
# отрицательное. Использовать это исключение в функции check_positive_number.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#
class NegativeNumberError(Exception):
    def __init__(self, num:int, message="Число отрицательное"):
        self.message = message
        super().__init__(self.message)
        self.num = num
    def __str__(self):
        return f'{self.num} -> {self.message}'        
#
def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number
# Пример использования функции
try:
    n=10
    print(check_positive_number(n)) # Корректное число, исключение не генерируется
    n=0
    print(check_positive_number(n))   # Корректное число, исключение не генерируется
    n=-5
    print(check_positive_number(n))  # Генерируется NegativeNumberError
except NegativeNumberError as e:
    print(f"Ошибка: {e}")
