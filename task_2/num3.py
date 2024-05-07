dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

a = set()
for key, value in dct.items():
    a.add(key)

b = set()
for key, value in dct.items():
    b.add(value)

c = a | b

print("Union:", c)
