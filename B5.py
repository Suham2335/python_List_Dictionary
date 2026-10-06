student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}

k = input("Enter a key: ")

if k in student:
    print(f"{k} exists in the dictionary")

else:
     print(f"{k} does not exist in the dictionary")