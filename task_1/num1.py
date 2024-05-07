while True:
    user_input = input("Введите число (выйти - ввод 'exit'): ")

    if user_input.lower() == 'exit':
        print("Программа завершена.")
        break

    if not user_input.isdigit():
        print("Ошибка: Введенное значение не является числом. Попробуйте снова.")
        continue

    print(f"Длина введенного числа: {len(user_input)}")
