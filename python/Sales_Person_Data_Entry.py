#Application for business to make changes to their system and record sales
#Manager should be able to add salespersons and their commission rate (create a class for salespersons)
class Salesperson:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

class Product:
    def __init__(self, name = [],  quantity = 0, price = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def appendProductName(name):
        print(type(name))
        name.append(name)

def DisplayOptions():
    print()
    print("Enter one of the following options (99 to end)")
    print("1 - Enter Salesperson Information")
    return int(input("Enter selection: "))
        
def Salesperson_Data_Entry():
    #capture the Salesperson's data
    print()
    name = input("Enter Salesperson's name: ")
    commission = float(input("Enter Salesperson's commission rate (5% = .05): "))
    salesperson = Salesperson(name, commission)
    print()
     #capture Salesperson's products sold  
    
    tax = float(input("Please enter the tax rate (2% = .02): "))
    Product.appendProductName(input("Please enter product name: "))
    print(Product.name)
    Product.price = float(input("Please enter product price: "))
    Product.quantity = int(input("Please enter how many products were purchased: "))

#add product
    #salesperson.append(Product)
        
    print(salesperson.name + " has sold " + str(Product.quantity) + Product.name + " !")
    print()
    want_to_add_product = input(print('Would you like to add another product?: Y/N '))
    if want_to_add_product.upper() == 'Y':
        print('made it here')
        Salesperson_Data_Entry()
    elif want_to_add_product.upper() == 'N':
        tax_item = Product.quantity * (tax * Product.price)
        net_total = Product.quantity * (tax_item + Product.price)
        gross_total = (Product.quantity * Product.price)
        commission_earned = Product.quantity * (commission * Product.price)

        print("The tax on this item is", format(tax_item, ".2f"))          
        print()          
        print("The total before tax is", format(gross_total, ".2f"))          
        print()          
        print("The overall total is", format(net_total, ".2f"))
        print()
        print("The commissoin earned is", format(commission_earned, ".2f"))
    else:
        want_to_add_product
        
    

    


#Application Starts here
print("Welcome to the Sales application :)")
print()

salesperson = ()
selection = DisplayOptions()

while selection != 99:
    if selection == 1:
       Salesperson_Data_Entry()
    else:
        print("Invalid, try again")

    selection=DisplayOptions()

print("Have a good day!")