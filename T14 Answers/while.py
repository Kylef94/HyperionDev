'''This program asks user to input a number, and keeps asking until user
inputs -1, at which point the average of all numbers entered (excluding the -1)
is then output'''

#intialize list to store numbers
num_list = []


#instruct user how to use program
print("This program will keep asking you for numbers until you input -1, at which point it will calculate the average")

#initialize user input variable

user_input = 0

#start loop and keep looping until input is -1
while user_input != -1:
    user_input = int(input("Please enter another number or input -1 to get the average:\n"))

    #ensures that when user inputs -1 it isn't included in the average, but all other numbers are
    if user_input != -1:
        num_list.append(user_input)

#calculate average, if user has not input anything would throw a ZeroDivision error, so using try except block to handle
try:
    average = sum(num_list) / len(num_list)

    # print answer
    print(f"The average of the numbers entered is {average}")

#if user has not input anything except -1, below block will inform user accordingly and
# catch the ZeroDivisonError thrown by interpreter
except ZeroDivisionError:
    print("You have not input any numbers, as such an average cannot be calculated")

