"""This program allows the user to either calculate the interest they
will earn on an investment, or what would be paid monthly for a home loan"""

import math

#get user input and put to all lowercase for comparison
user_choice = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n"
                    "investment - to calculate the amount of interest you'll earn on your investment\n"
                    "bond - to calculate the amount you'll have to pay on a home loan\n")
user_choice = user_choice.lower()

#show error if choice input is not valid
if user_choice != "investment" and user_choice != 'bond':
    print("Apologies, your input was invalid, please try again and ensure you type either 'investment' or 'bond' as your option")

#calculate interest earned on investment as per user inputs
elif user_choice == "investment":
    inv_amt = int(input("Please enter the amount you plan to invest\n"))
    int_rate = float(input("Please enter the interest rate without % (e.g. if 8.5% interest then enter 8.5)\n"))
    int_rate = int_rate / 100
    years = float(input("Please input how many years the funds will be invested for\n"))
    interest = input("Please indicate whether you want simple or compound interest (simply enter 'simple' or 'compound')\n")
    interest = interest.lower()

    #take inputs and calculate appropriately using either simple or compound interest as chosen by user
    if interest == 'simple':
        end_amt = inv_amt * (1 + int_rate * years)

    elif interest == 'compound':
        end_amt = inv_amt * math.pow((1 + int_rate), years)

    #throw error if input invalid
    else:
        print("Apologies, your input was invalid, please try again and ensure you type either 'simple' or 'compound' as your option")

    #if input was valid then output answer
    print(f"Your ending amount would be {end_amt:.2f}")
    print(f"The total interest earned would be {end_amt - inv_amt:.2f}")




#calculate monthly bond payment and output
elif user_choice == "bond":
    house_val = int(input("Please enter the current house value\n"))
    int_rate = float(input("Please enter the interest rate without % (e.g. if 8.5% interest then enter 8.5)\n"))
    months = int(input("Please enter how many months you plan to take to repay the bond\n"))

    #adjust interest rate to be both % and monthly
    int_rate = int_rate / 100
    monthly_int = int_rate / 12

    #calculate answer and output
    monthly_pmt = (monthly_int * house_val) / (1 - (1 + monthly_int) ** (0 - months))
    print(f"your monthly payment will be {monthly_pmt:.2f}")
