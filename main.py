import random

# declaring the variables globally
item_name = ''
item_description = ''
item_price = 0
item_quantity = 0
item_ID = ''


def product_registration():  # register the product function
    global item_name, item_description, item_price, item_quantity, item_ID

    item_name = input('Type the product name: ')  # add a function to not allow the name to be null

    item_description = input('Type a description for the product (optional): ')

    try:  # error handling
        item_price = float(input('Type the price of the product: '))  # !!add a function to allow the user to type ','
        # instead of '.' and make it work as well!!
    except ValueError:  # error when you try to insert a non number inside a float or int
        print('The value inserted was does not correspond to a number')
    item_price = "{:.2f}".format(item_price)  # force to print the number with 2 decimal places

    try:  # error handling
        item_quantity = int(input('Type the quantity to be sold: '))  # !!add a function to allow the user to type ','
        # instead of '.' and make it work as well!!
    except ValueError:  # error when you try to insert a non number inside a float or int
        print('The value inserted was does not correspond to a number')

    ID = ''

    for i in range(5):
        number = random.randint(0, 9)  # create a random number between 0 and 9 to create the ID
        ID += str(number)  # get the 'number' variable and append it to the 'ID' variable
    item_ID = f'#{ID}'  # just put a '#' before the ID


product_registration()

item_price = str(item_price)

print(f'Item name: {item_name}\nItem description: {item_description}\nItem price: {item_price}\nItem quantity: '
      f'{item_quantity}\nItem ID: {item_ID}')
