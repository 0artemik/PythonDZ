while True:

    user_input = input("Введите число: ")

    if not user_input.isdigit():
        print("Введено не число.")
        continue

    user_num = int(user_input)
    break

sum_neg = 0
sum_pos = 0

print(f"Числа в интервале [-{user_num}, {user_num + 1}]:")
for i in range(-user_num, user_num+1):
    print(i, end=" ")

    if i < 0:
        sum_neg += i
    elif i > 0:
        sum_pos += i

print("Negative sum: ", sum_neg)
print("Positive sum: ", sum_pos)
