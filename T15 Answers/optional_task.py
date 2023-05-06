
#get user input
num = int(input("Please enter a number\n"))

#if number entered is greater than 10, outputs the users input as many times as its value
if num > 10:
    for i in range(0, num):
        print(num)

#if num less than or equal to 10, too small for loop as per specification
else:
    print("Sorry, too small")

