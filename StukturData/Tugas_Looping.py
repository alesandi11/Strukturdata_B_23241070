for i in range(1, 6):
    print(i)
i = 1
while i <= 5:
    print(i)
    i += 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-" * 10)
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    if i == 8:
        break
    print(i)
    i += 1