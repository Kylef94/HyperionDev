#initialise list with menu items
menu = ["Coffee", "Cake", "Sandwich", "Tea"]

#initialise dictionary with stock quantities
stock = {"Coffee": 20,
         "Cake": 30,
         "Sandwich": 10,
         "Tea": 20
         }
#initialise price dictionary
price = {"Coffee": 2,
         "Cake": 3.5,
         "Sandwich": 5,
         "Tea": 2
         }

#var for total stock value
total_stock = 0

#iterate through menu and for each item multiply its price by quantity in stock, then add this  to total stock value
for item in menu:
    stock_value = stock[item] * price[item]
    total_stock += stock_value

#output result
print(total_stock)