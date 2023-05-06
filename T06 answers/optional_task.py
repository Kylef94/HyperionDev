import math
''' This program asks the user to input the measurements for the 3 
sides of a triangle, then calculates its area '''

#get input
print("This program calculates the area of a triangle once you input measurements for its 3 sides")
side1 = float(input("Please enter the length of the first side of the triangle\n"))
side2 = float(input("Please enter the length of the second side of the triangle\n"))
side3 = float(input("Please enter the length of the third side of the triangle\n"))

#calculate area
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print(f"the area is {area: .2f}")