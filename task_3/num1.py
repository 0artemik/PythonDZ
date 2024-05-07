Addition = lambda a, b: a + b
Subtraction = lambda a, b: a - b
Multiplication = lambda a, b: a * b
Exponentiation = lambda a, b: a ** b
def Division(a, b):
    if b == 0:
        raise ValueError("Вы не можете разделить на 0")
    return a / b

while True:
    userInput = input("Введите операцию, которую необходимо выполнить (пример: 2/2, 3**5), или выйдите:").split(" ")
    if userInput == "Выход":
        break
    elif len(userInput) != 3:
        print("Введена неверная операция")
        continue
    elif not userInput[0].isdigit() or userInput[1].isdigit():
        print("Введена неверная операция")
        continue
    else:
        userInput[0] = int(userInput[0])
        userInput[2] = int(userInput[2])

    if userInput[1] == "+":
        print(Addition(userInput[0], userInput[2]))
    elif userInput[1] == "-":
        print(Subtraction(userInput[0], userInput[2]))
    elif userInput[1] == "*":
        print(Multiplication(userInput[0], userInput[2]))
    elif userInput[1] == "**":
        print(Exponentiation(userInput[0], userInput[2]))
    elif userInput[1] == "/":
        try:
            print(Division(userInput[0], userInput[2]))
        except ValueError:
            print("Вы не можете разделить на 0")
            continue
    else:
        print("Введена неверная операция")
        continue