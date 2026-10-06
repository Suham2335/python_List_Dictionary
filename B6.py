marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55,
}

print(marks.items())


print(sum(marks.values()))
print(sum(marks.values())/len(marks.values()))
print(max(marks.values()))
print(min(marks.values()))
print(marks.keys())

print(list(marks.keys())[list(marks.values()).index(max(marks.values()))])
