fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple",
    "mango", "orange", "banana"
]

count ={}

for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
       count[fruit] = 1

print(count)


