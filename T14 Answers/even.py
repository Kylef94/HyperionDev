"""This program takes an integer input from the user and prints
all even numbers from 1 up to (and possibly including) the number input"""

#get input from user
user_num = int(input("Please enter a whole number, if you enter a decimal then any digits after the decimal point will be ignored\n"))

#initialize counter for while loop
n = 2

#start loop and print all even numbers up to(and including) user_num
while n <= user_num:
    print(n)
    n += 2
