'''this program asks user for an integers, checks if it is divisible
by 2 or 5, then informs user accordingly'''

num = int(input("Please enter a whole number"))

if num % 2 == 0 and num % 5 == 0:
    print("This number is divisible by both 2 and 5!")
elif num % 2 == 0 or num % 5 == 0:
    print("This number is divisible either by 2 or 5, but not both!")

if num % 2 != 0 and num % 5 != 0:
    print("This number is not divisible by either 2 or 5!")