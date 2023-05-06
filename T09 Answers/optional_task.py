'''calculates monthly wages for a department store employee'''

#ask if user is employee or manager and validate input

emp_type = int(input("Please indicate whether you are an employee or a manager:\n"
                     "1: Employee\n"
                     "2: Manager\n"))


#if employee ask for gross sales and calculate wages(£2k per month + 8% commission on gross sales)

if emp_type == 1:
    sales = int(input("Please enter your gross sales for the month\n"))
    wage = 2000 + (sales * 0.08)

#if manager ask for hours worked and calculate wages(£40 per hour)

elif emp_type == 2:
    hours = int(input("Please enter your hours worked for the month\n"))
    wage = hours * 40

#error in case user chose invalid input
else:
    print("Sorry, the option you input wasn't valid, please try again\n")

#print calculated wage

print(f"Thank you! your monthly wage should be {wage}")