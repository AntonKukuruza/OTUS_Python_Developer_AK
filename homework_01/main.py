"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


squares = power_numbers(1, 2, 5, 7)
print(squares)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(*numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

def filter_numbers(numbers = [], filter_type = None):
    if filter_type == ODD:
        return [number for number in numbers if number % 2]
    
    elif filter_type == EVEN:
        return [number for number in numbers if number % 2 == 0]    
    
    elif filter_type == PRIME:
        prime_num = []
        for number in numbers:
            for div in range(2, (number // 2) + 1):
                if number % div == 0:
                    break
            else:
                prime_num.append(number)
        return prime_num
        
filtered_numbers_odd = filter_numbers([1, 2, 3], ODD)
print(f"odd: {filtered_numbers_odd}")

filtered_numbers_even = filter_numbers([2, 3, 4, 5], EVEN)
print(f"even: {filtered_numbers_even}")

filtered_numbers_prime = filter_numbers([1, 3, 4, 5, 6, 7, 8], PRIME)
print(f"prime: {filtered_numbers_prime}")

