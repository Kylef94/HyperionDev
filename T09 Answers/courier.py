'''Calculates the cost of sending a parcel based on user-inputs'''

#get product price and distance and initialize shipping cost variable
product_cost = float(input("Please enter the price of the package you plan to buy\n"))
distance = float(input("Please enter the shipping distance in kms"))
shipping_cost = 0

#ask user if they want air or freight shipping and update shipping cost accordingly
air_or_freight = int(input("Please select how you will ship the product from the options below\n"
                           "1: Air shipping(£0.36 per km)\n" 
                           "2: Freight shipping(£0.25 per km)\n"))

if air_or_freight == 1:
    shipping_cost = distance * 0.36

elif air_or_freight == 0:
    shipping_cost = distance * 0.25

else:
    print("Sorry, the number you entered was not valid, please try again")

#ask user what insurance option they want and update shipping cost accordingly
insurance = int(input("Please select how you will insure the product from the options below\n"
                           "1: Full Insurance(£50)\n"
                           "2: Limited insurance(£25)\n"))

if insurance == 1:
    shipping_cost += 50

elif insurance == 0:
    shipping_cost += 25

else:
    print("Sorry, the number you entered was not valid, please try again")

#ask user what gift option they want and update shipping cost accordingly
gift = int(input("Please select if this is a gift from the options below\n"
                           "1: Gift(£15)\n"
                           "2: No gift(£0)\n"))

if gift == 1:
    shipping_cost += 15

elif gift == 0:
    shipping_cost += 0

else:
    print("Sorry, the number you entered was not valid, please try again")

#ask user what shipping they want and update shipping cost accordingly
priority = int(input("Please select shipping priority from the options below\n"
                           "1: Priority delivery(£100)\n"
                           "2: Standard delivery(£20\n"))

if priority == 1:
    shipping_cost += 100

elif priority == 0:
    shipping_cost += 20

else:
    print("Sorry, the number you entered was not valid, please try again")

total = product_cost + shipping_cost

print(f'Thank you! Your product cost was £{product_cost}, and your shipping costs come to £{shipping_cost}, the total cost is £{total}')