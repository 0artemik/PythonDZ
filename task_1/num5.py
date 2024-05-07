while True:
    name = input("Введите ваше имя: ")
    if name.isalpha():
        break
    else:
        print("Вы ввели не имя")

while True:
    surname = input("Введите фамилию: ")
    if surname.isalpha():
        break
    else:
        print("Вы ввели не фамилию")

while True:
    age = input("Введите ваш возраст: ")
    if age.isdigit():
        break
    else:
        print("Вы ввели не возраст")

print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")
