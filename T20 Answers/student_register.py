'''This program generates a register of students for an exam venue'''

#get number of students to register
num_students = int(input("Please enter how many students will be registered: "))

#initialise list to hold student id numbers, first entry will act as columns heading on file to make it clear what file is for

student_ids = ["Student ID          Signature\n"]

#loop through students and ask for their id number
for i in range(num_students):
    id = input("Please enter your student ID number: ")

    #add line for signatures and append to list
    id = id + "             ____________________\n"
    student_ids.append(id)

#write to file reg_form.txt
with open('reg_form.txt', 'w') as file:
        file.writelines(student_ids)

