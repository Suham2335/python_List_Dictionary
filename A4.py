numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_five =[numbers[i] for i in range(5)]

last_five = [numbers[i] for i in range(-5,0)]

index2_6 =[numbers[i] for i in range(2,7)]

every2nd = [numbers[i] for i in range(0,10,2)]

numbers.reverse()



print(first_five)
print(last_five)
print(index2_6)
print(every2nd)
print(numbers)
