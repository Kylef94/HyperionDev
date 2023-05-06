'''This is a program that asks the user for their full name
then validates that this was entered'''

#get user input and set flag for while loop
user_name = input("Please enter your full name (name and surname)\n")
valid_name = False

#keeps looping until valid full name is entered
while not valid_name:
    #checks if input has digits, if so cannot be user full name
    if any(char.isdigit() for char in user_name):
        user_name = input("You have entered numbers, please enter your full name (name and surname) using letters\n")

    #checks for empty string
    elif len(user_name) == 0:
        user_name = input("You haven't entered anything, please enter your full name (name and surname)\n")

    #checks if input is too short  to be a full name
    elif len(user_name) < 4:
        user_name = input("You have entered less than 4 characters, please enter your full name (name and surname)\n")

    #splits username by space, if returned list has length 1 then user only input 1 name, if 2 then means 2 names were input which is what we want
    elif len(user_name.split(' ')) == 1:
        user_name = input("You have entered only 1 name, please enter your full name (name and surname)\n")

    #checks if input is too long to be a first and last name, set limit at 25 characters
    elif len(user_name) > 25:
        user_name = input("You have entered more than 25 characters, please ensure you only enter your full name (name and surname)\n")

    #if above validation met, exit loop and print response
    else:
        valid_name = True
        print("Thank you for entering your name")