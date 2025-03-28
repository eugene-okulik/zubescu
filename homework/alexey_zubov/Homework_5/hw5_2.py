s1 = 'результат операции: 42'
s2 = 'результат операции: 514'
s3 = 'результат работы программы: 9'


# вариант через функцию
def get_number(s: str) -> int:
    idx = s.index(':') + 2
    num = s[idx:]
    return int(num)


num1 = get_number(s1) + 10
num2 = get_number(s2) + 10
num3 = get_number(s3) + 10

print(num1, num2, num3)
