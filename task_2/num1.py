num_elements = int(input("Введите количество чисел в списке: "))

numbers = []

for i in range(num_elements):
    element = input("Введите число или строку: ")
    numbers.append(element)

power = int(input("Степень: "))

print(f"Числа: {numbers}, возведенные в степень: {power}")
for num in numbers:
    if num.isdigit():
        num = int(num)
        powered_num = num ** power
        print(powered_num)
    else:
        try:
            num = int(num)
        except ValueError:
            pass
