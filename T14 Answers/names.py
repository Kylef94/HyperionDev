'''This program takes a list of student names from the user
and keeps asking until user enters "Stop", at which point
program will output the number of names user has input'''

#initialise count variable for student names
student_count = 0

#intialize variable for user input
student_name = input("Please enter the students name\n")

#start loop and keep looping until user inputs stop

while student_name != "Stop":
    student_name = input("Please enter the next students name\n")
    student_name = student_name.capitalize()
    if student_name != "Stop":
        student_count += 1

#print total student count once user has input "stop"
print(f"The total number of students is {student_count}")