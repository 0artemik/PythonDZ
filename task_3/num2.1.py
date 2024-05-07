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

def Mult(a: list, b: int = 2) -> list:
    l1 = []
    for i in range(len(a)):
        l1.append(l[i] * b)
    return l1

print(Mult(l))
print(Mult(l, n))
