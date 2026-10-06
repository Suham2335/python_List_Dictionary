numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)