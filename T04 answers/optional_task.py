'''gets users input for 2 numbers,
prints both numbers then switches their positions and prints again'''

#get user input
num1 = input("Please enter a number\n")
num2 = input("Please enter another number\n")

print(f'number 1: {num1}')
print(f'number 2: {num2}')

#swap variables
temp = num1
num1 = num2
num2 = temp

print(f'number 1: {num1}')
print(f'number 2: {num2}')