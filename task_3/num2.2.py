while True:
    l = input("Введите список чисел, разделенных пробелами:").split(" ")
    try:
        for i in range(len(l)):
            if l[i].isdigit():
                l[i] = int(l[i])
            else:
                raise ValueError("Неправильный тип данных")
                break
    except ValueError:
        print("Введен неверный список")
    else:
        break

while True:
    n = input("Введите множитель:")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Введен неверный множитель")

Mult = lambda a, b = 2: [a[i] * b for i in range(len(a))]

print(Mult(l))
print(Mult(l, n))