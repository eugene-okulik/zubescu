import sys


def fibonacci_generator():
    first = 0
    second = 1

    yield first
    yield second

    while True:
        current = first + second
        yield current
        first, second = second, current


def print_value(num):
    count = 1
    for number in fibonacci_generator():
        if count == num:
            """
            без этого появляется ошибка для больших чисел
            ValueError: Exceeds the limit (4300 digits)
            """
            if num > 10000:
                sys.set_int_max_str_digits(100000)
            print(number)
            break
        count += 1


print_value(5)
print_value(200)
print_value(1000)
print_value(100000)
