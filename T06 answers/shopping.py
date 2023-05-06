#get user inputs for products and prices
product1 = input("Please enter a product name\n")
product2 = input("Please enter another product name\n")
product3 = input("Please enter a final product name\n")

price1 = float(input(f'Please enter the price of {product1}\n'))
price2 = float(input(f'Please enter the price of {product2}\n'))
price3 = float(input(f'Please enter the price of {product3}\n'))

#sum prices and average
sum = price1 + price2 + price3
avg = sum / 3

print(f'The total of {product1}, {product2}, {product3} is £{sum} and the average price is {avg: .2f}')
