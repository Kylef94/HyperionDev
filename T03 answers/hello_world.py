
#get users name
name = input('Hello! Please enter your name\n')

#check if user entered a number instead, and ask for their name until valid input given
while name.isdigit():
    name = input('You entered a number, please only enter your name\n')

print(name)

#get users age
age = input('Thank you! Please enter your age\n')

#check if user entered a non-number, and ask for their age until valid input given
while not age.isdigit():
    age = input('You entered letters, please enter your age in whole numbers\n')

print(age)
print("Hello World!")