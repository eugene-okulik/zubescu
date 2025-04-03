from random import choice, randrange

salary = int(input('Enter salary: '))
bonus = choice([False, True])

if bonus:
    salary += randrange(1, 9999)
print(salary)
