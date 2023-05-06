'''This program asks the user for the shape of a building and
its dimensions, then calculates the area of its foundation
'''

import math

print("This program will calculate the are of a building foundation")
building = int(input("Please choose the type of building by entering the appropriate number\n"
                     "1: Square\n"
                     "2: rectangular\n"
                     "3: circular\n"))

#calculate square building
if building == 1:
    length = float(input("Thank you, Please enter the buildings length\n"))
    area = length ** 2
    print(f"The area of the building is {area}")

#rectangular building
elif building == 2:
    length = float(input("Thank you, Please enter the buildings length\n"))
    width = float(input("Thank you, Please enter the buildings width\n"))
    area = length * width
    print(f"The area of the building is {area}")

#circular building
elif building == 3:
    radius = float(input("Thank you, Please enter the buildings radius\n"))
    area = (radius ** 2) * math.pi
    print(f"The area of the building is {area}")

else:
    print("Sorry, the option you have selected is not valid, please try again using numbers 1,2 or 3")