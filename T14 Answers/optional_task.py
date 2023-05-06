'''This program asks the user to input a number less than or equal to 100,
if input is above 100, program will keep asking until valid input is entered,
once this is done program will adjust output based on whether input is odd or even'''

#get user input
user_input = int(input("Please input a number less than or equal to 100\n"))

#keeps looping until user enters a number less than or equal to 100, if above input was greater than 100
while user_input > 100:
    user_input = int(input("You entered a number greater than 100, please input a number less than or equal to 100\n"))

#checks if number entered was even or odd, if even will print double or triple
# the numbers value, based on if it is even or odd respectively
if user_input % 2 == 0:
    print(user_input * 2)

else:
    print(user_input * 3)



