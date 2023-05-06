#get input from user
user_num = int(input("Please enter a whole number, if you enter a decimal then any digits after the decimal point will be ignored\n"))

#initialize counter for while loop
n = 2

#start loop and print all even numbers up to(and including) user_num
#logical error is that the loop only increments by 1, so will actually print all numbers instead of only even numbers
while n <= user_num:
    print(n)
    n += 1