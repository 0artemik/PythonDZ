import random

number = random.randint(1, 100)

if number % 2 == 0:
    print(f"Чётное число {number}")
else:
    print(f"Нечётное число {number}")
