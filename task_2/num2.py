while True:
    user_input = input("Введите строку (без пробелов): ")

    if ' ' in user_input:
        print("Строка  введена не верно")
        continue

    user_input = user_input.lower()
    char_count = {}

    for char in user_input:
        char_count[char] = user_input.count(char)

    print("Подсчет символов {символ: количество символов}: ", char_count)
    break
