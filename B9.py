students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

print(students)

print(students[101])
print()
students[103]["course"] = "C"
print(students[103])

students[104] = {
        "name": "Alex",
        "age": 19,
        "course": "c#"
    }  
print()
students.pop(101)
print(students)

n = int(input("Enter id: "))
print(f" Student details of id {n} is {students[n]}")