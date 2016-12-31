

highest = 0
second_highest = 0
third_highest = 0
fourth_highest = 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

for number in numbers:
    if number > highest:
        number = highest
    elif (highest > second_highest) and (second_highest > third_highest) and (third_highest > fourth_highest):
        highest = number
    elif (second_highest > highest) and (second_highest > third_highest) and (third_highest > fourth_highest):
        number = second_highest
    else:
        number = third_highest
    print(highest, second_highest)

#    if (num1 > num2) and (num1 > num3):
#        largest = num1
#    elif (num2 > num1) and (num2 > num3):
#        largest = num2
#    else:
#        largest = num3
