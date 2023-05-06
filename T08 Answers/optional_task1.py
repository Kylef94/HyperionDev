'''takes integer input from user, and checks if number is odd or even'''

user_input = int(input("Please enter a whole number, if number has a decimal point any digits afterwards will be ignored"))

if user_input % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd")