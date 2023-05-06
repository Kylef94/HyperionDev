#imports
import os

#functions

def calculate(num1, num2, operation):
    """This function handles a single calculation after checking that the operation is valid, and writes the answer to a file"""

    #list of valid operations
    valid_ops = ['+', '-', '/', '*']

    #check operator is valid
    if operation not in valid_ops:
        return "Invalid operator entered, please try again!"

    #logic for calculations
    match operation:
        case '+':
            ans = num1 + num2

        case '-':
            ans = num1 - num2

        case '/':
            #avoids division by 0 error
            if num2 == 0:
            return "Error: This leads to division by 0"
			
            ans = num1 / num2

        case '*':
            ans = num1 * num2

    #creates a string of the formula with answer for input to text file
    equation = f"{num1} {operation} {num2} = {ans}\n"

    #try to append to existing file, if not create new one
    try:
        with open("answers.txt", 'a') as file:
            file.writelines(equation)

    except FileNotFoundError:
        with open("answers.txt", 'w') as file:
            file.writelines(equation)

    #finally, return answer to user
    return ans

def mass_calc(filename):
    """This function handles calculations from files and outputting to user"""
    #check if file valid and open
    try:
        with open(filename, 'r') as file:
            formulas = file.readlines()

    except FileNotFoundError:
        return "The file name as entered could not be found, please try again"

    #loop through calculations
    for f in formulas:
        #try to split each line into operators, else throw and error
        try:
            num1, operation, num2 = f.split(' ')

        except ValueError:
            return "The file format could not be read, please ensure each line in formatted as <num1> <operation> <num2> " \
                   "and each formula is on its own line"

        #if all valid then do calculations
        num1, num2 = int(num1), int(num2) #conv to int
        ans = calculate(num1, num2, operation)

        #create output string and print
        output = f"{num1} {operation} {num2} = {ans}\n"
        print(output)


#main program logic


#get user input, loop until valid input entered

while True:
    option = input("Please select from the options below (enter number as appropriate):\n"
               "1. manually input a formula to calculate\n"
               "2. mass calculate formulas from file\n")
    if option != '1' and option != '2':
        print("Invalid option selected, please try again")
        continue
    else:
        break


#logic for error checking and getting further inputs from user
match option:
    #user wants to input manually
    case '1':
        #get number and operator inputs from the user
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            operation = input("Please indicate how to calculate the answer, the options are:\n"
                              "addition +\n"
                              "subtraction -\n"
                              "division /\n"
                              "multiplication *\n")
            #call function to calculate and output
            ans = calculate(num1, num2, operation)
            print(ans)

        except ValueError:
            print("One of your inputs was invalid, please try again")

    #user wants to read from file
    case '2':

        #loops until valid filename entered
        while True:
            filename = input("Please enter the name of the file and ensure it is in the same folder as this program")
            #if file not found raise error and loop
            if not os.path.exists(filename):
                print("The file could not be found, please check the filename and try again")
                continue
            else:
                break
        #once valid filename input, call function
        mass_calc(filename)









