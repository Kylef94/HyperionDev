'''This program takes a year as input from the user, and a number of years
to check, will then loop through each year and output if that year is a leap year'''

#get year input from user
start_year = int(input("What year do you want to start with?\n"))
num_of_years = int(input("How many years do you want to check?\n"))

#calculate last year to check for range
end_year = start_year + num_of_years

#loop through years and check if it is a leap year, and inform user accordingly
for year in range(start_year, end_year):

    #leap years are multiples of 4, so if year module 4 is 0 then that means it is a leap year
    if year % 4 == 0:
        print(f"{year} is a leap year")

    else:
        print(f"{year} is not a leap year")





