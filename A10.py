marks = [75, 82, 68, 90, 55, 88, 72, 95]

print(marks)

print(sum(marks))
print(sum(marks)/len(marks))
print(max(marks))
print(min(marks))
count = 0
for item in marks:
    if item>=75:
        count+=1
print(count)     

print()
marks.sort()
print(marks)

m = int(input("Enter another students marks: "))
marks.append(m)
marks.sort()
print(marks)