'''This program takes a numeric input from the user, then prints out
the times table for that number'''

#instruct user
print("This program will take a whole number input, and output the times table from 1 to 12")

#get user input
user_input = int(input("Please enter a whole number\n"))

print(f"Thank you! the {user_input} times table is as follows:")

#uses range to loop from 1 to 12, then uses f string to output calculations
#task specification starts at 6 x 1, so starting range from 1 onwards
for i in range(1,13):
    print(f"{user_input} x {i} = {user_input * i}")