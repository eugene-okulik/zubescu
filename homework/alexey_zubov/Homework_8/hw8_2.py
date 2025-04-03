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


def print_generator(num):
    count = 1
    for number in fibonacci_generator():
        if count == num:
            """
            без этого появляется ошибка для больших чисел
            ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
            """
            if num > 10000:
                sys.set_int_max_str_digits(100000)
            print(number)
            break
        count += 1


print_generator(5)
print_generator(200)
print_generator(1000)
print_generator(100000)
