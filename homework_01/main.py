"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    # variant 1 - cycle
    # result = []
    # for number in args:
    #     result.append(number**2)
    # return result

    # variant 2 - list comprehension
    # return [number**2 for number in args]

    # variant 3 - iterator
    return list(map(lambda number: number**2, args))



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    Функция, которая на вход принимает число и возвращает True, если оно простое,
    и False в противном случае.
    Просто́е число́ — натуральное число, имеющее ровно два различных натуральных делителя.
    Другими словами, натуральное число p является простым, если оно отлично от 1 и делится
    без остатка на 1 и на само p (Wikipedia)"""
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda item: item % 2 == 1, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda item: item % 2 == 0, numbers))
    else:
        return list(filter(is_prime, numbers))
