'''takes user inputs and outputs a string containing user inputs'''

#get user inputs

name = input("Please enter your name\n")
age = input("Please enter your age\n")
house_no = input("Please enter your house number\n")
street_name = input("Please enter your street name\n")

#print output

print(f'This is {name.capitalize()}, '
      f'they are {age} years old and live at house number {house_no} on {street_name.capitalize()}')