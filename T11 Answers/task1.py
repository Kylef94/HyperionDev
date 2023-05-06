'''This program declares 3 integer variables then runs comparisons on each'''

num1 = 500
num2 = 2000
num3 = 50

#returns largest value from num1 and num2
if num1 > num2:
    print(num1)
elif num1 == num2:
    print("num1 and num2 are equal")
else:
    print(num2)

#returns whether num1 is even or not

if num1 % 2 == 0:
    print("num1 is even")
else:
    print("num1 is odd")

#sort numbers largest to smallest

largest = 0
middle = 0
smallest = 0

#case where num1 is largest


if num1 > num2 and num1 > num3:
    largest = num1
    if num2 > num3:
        middle = num2
        smallest = num3
    else:
        middle = num3
        smallest = num2

elif num2 > num1 and num2 > num3:
    largest = num2
    if num1 > num3:
        middle = num1
        smallest = num3
    else:
        middle = num3
        smallest = num1

else:
    largest = num3
    if num1 > num2:
        middle = num1
        smallest = num2
    else:
        middle = num2
        smallest = num1

print(largest, middle, smallest)