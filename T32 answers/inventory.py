
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """Class constructor"""
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """getter for cost attr."""
        return self.cost

    def get_quantity(self):
        """getter for quantity attr."""
        return self.quantity

    def restock(self, qty):
        '''handles restock for quantity attribute'''
        self.quantity += qty

    def get_value(self):
        '''getter for value'''
        return self.quantity * self.cost

    def __str__(self):
        """returns string for prints"""
        return f"Product: {self.product}\n" \
               f"Code: {self.code}\n" \
               f"Country: {self.country}\n" \
               f"Quantity: {self.quantity}\n" \
               f"Cost: £{self.cost}"

    def to_file(self):
        """returns string for saving to file"""
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}\n"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list.
    '''
    try:
        with open("inventory.txt", "r") as f:
            data = f.readlines()
            for d in data[1:]:
                try:
                    country, code, product, cost, qty = d.split(',')

                except ValueError:
                    print(f"line {d} in file could not be parsed and was not added to the inventory list")
                    continue

                shoes = Shoe(country, code, product, cost, qty)
                shoe_list.append(shoes)
    except FileNotFoundError:
        save_shoes_data()
        read_shoes_data()


def save_shoes_data():
    """saves current inventory to file"""
    with open("inventory.txt", 'w') as f:
        to_save = [shoe.to_file() for shoe in shoe_list]
        f.write("Country,Code,Product,Cost,Quantity\n")
        f.writelines(to_save)

def capture_shoes():
    '''
    This function allows a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("Please enter the country")
    code = input("Please enter the product code")
    product = input("Please enter the product name")
    cost = input("Please enter the cost per unit")
    qty = input("Please enter the quantity in stock")

    shoes = Shoe(country, code, product, cost, qty)
    shoe_list.append(shoes)
    save_shoes_data()
    print(f"{product} has been added to inventory!")


def view_all():
    ''' This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''

    for shoe in shoe_list:
        print(shoe)
        print("----------------------")


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked.
    '''
    min_qty = float('inf')
    low_shoes = None

    for shoe in shoe_list:
        if shoe.quantity < min_qty:
            min_qty = shoe.quantity
            low_shoes = shoe

    print(f"The shoes currently running low on stock are {low_shoes.product}, their quantity is currently {low_shoes.quantity}")
    restock_choice = input("Would you like to restock these shoes? Y/N").capitalize()

    if restock_choice == "Y":
        qty_to_add = int(input("How many units would you like to add to the stock?"))
        low_shoes.restock(qty_to_add)
        save_shoes_data()

def search_shoe(code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe

    return "Error: a shoe with this code could not be found"


def value_per_item():
    '''
    This function will calculate the total value for each item and print to console
    '''
    for shoe in shoe_list:
        print(f"Product: {shoe.product}")
        print(f"Quantity: {shoe.quantity}")
        print(f"Cost: £{shoe.cost}")
        print(f"Value: £{shoe.get_value()}")
        print("-------------------")

def highest_qty():
    '''
    Determines the product with the highest quantity and
    print this shoe as being for sale.
    '''
    max_qty = 0
    high_shoes = None

    for shoe in shoe_list:
        if shoe.quantity > max_qty:
            max_qty = shoe.quantity
            high_shoes = shoe

    print(f"{high_shoes.product} are currently for sale!")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

read_shoes_data()

#Menu loop
while True:
    user_choice = input("Please select from the options below:\n"
                        "va - View all\n"
                        "s - search shoes by code\n"
                        "c - capture shoes\n"
                        "v - stock value per item\n"
                        "r - restock\n"
                        "sa - view shoes currently on sale\n"
                        "e - exit\n")

    match user_choice:
        case 'va': # view all items
            view_all()

        case 's': #search for product
            code = input("Please input the product code")
            print(search_shoe(code))

        case'c': #capture shoes and save to inventory
            capture_shoes()

        case 'v': #returns total stock value of each inventory item
            value_per_item()

        case 'r': #gets lowest item and offers to restock
            re_stock()

        case 'sa': #gets product with highest quantity and puts it on sale
            highest_qty()

        case 'e': #exit
            exit(0)

        case _: #invalid input
            print("Invalid input entered, please try again")
            user_choice = input("Please select from the options below:\n"
                                "va - View all\n"
                                "s - search shoes by code\n"
                                "c - capture shoes\n"
                                "v - stock value per item\n"
                                "r - restock\n"
                                "sa - view shoes currently on sale\n"
                                "e - exit\n")