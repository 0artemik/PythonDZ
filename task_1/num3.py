x = input("Введите трехзначное число, в котором все цифры разные:")
if x.isdigit():
    x1 = int(int(x) / 100)
    x2 = int((int(x) % 100) / 10)
    x3 = int(int(x) % 10)
    if len(x) == 3 and x1 != x2 != x3:
        print(f"Числовые перестановки {x}:")
        print(x1, x2, x3)
        print(x1, x3, x2)
        print(x2, x1, x3)
        print(x2, x3, x1)
        print(x3, x1, x2)
        print(x3, x2, x1)
    else:
            print("Вы ввели не трехзначный номер или некоторые цифры совпадают")
else:
    print("Вы не ввели трехзначное число")
