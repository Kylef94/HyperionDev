'''This program asks the user to input their age,
then checks this age against given ranges (18+, 16-18, 15 or younger)
and prints appropriate output'''

#get user input
age = int(input("Please enter your age\n"))

#check age and print appropriate response

if age >= 18:
    print("You are old enough!")

elif 16 < age < 18:
    print("Almost there.")
else:
    print("You're just too young!")

