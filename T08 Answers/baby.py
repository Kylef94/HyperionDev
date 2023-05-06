'''This program asks the user to input their date of birth,
then checks current year to calculate users age, this will
decide if they can enter a party'''

from datetime import date

#get user input
year_born = int(input("Please enter the year you were born\n"))

#get current year using date module
current_year = date.today().year

#check age and output
user_age = current_year - year_born

if user_age >= 18:
    print("Congrats you are old enough.")
else:
    print("Sorry you are not old enough.")

