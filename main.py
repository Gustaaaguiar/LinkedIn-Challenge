import random
import qrcode

# declaring the variables globally
item_name = ''
item_description = ''
item_price = 0
item_quantity = 0
item_ID = ''


def set_name():  # Everything is ok!
    global item_name
    item_name = input('Type the product name: ')  # add a function to not allow the name to be null

    if item_name == '':
        print('Name cannot be null')
        set_name()


def set_price():  # Everything is ok!
    global item_price
    try:  # error handling
        item_price = float(input('Type the price of the product: ').replace(',', '.'))
    except ValueError:  # error when you try to insert a non number inside a float or int
        print('The value inserted was does not correspond to a number')
    item_price = "{:.2f}".format(item_price)  # force to print the number with 2 decimal places
    if item_price == '':
        print('Price cannot be null')
        set_price()


def set_quantity():  # Everything is ok!
    global item_quantity
    try:  # error handling
        item_quantity = int(input('Type the quantity to be sold: '))
    except ValueError:  # error when you try to insert a non number inside a float or int
        print('The value inserted was does not correspond to an integer')
        set_quantity()
        if item_quantity == '':
            print('Quantity cannot be null')
            set_quantity()


def set_ID():  # Everything is ok!
    global item_ID
    ID = ''

    for i in range(5):
        number = random.randint(0, 9)  # create a random number between 0 and 9 to create the ID
        ID += str(number)  # get the 'number' variable and append it to the 'ID' variable
    item_ID = f'#{ID}'  # just put a '#' before the ID


def create_qr():
    qr = qrcode.QRCode(
        version=1,  # determines the size of the qrcode
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,  # determines the size of the boxes
        border=2,  # determines the thickness of the border
    )

    qr.add_data(f'Item name: {item_name}\nItem description: {item_description}\nItem price: R${item_price}\n'
                f'Item quantity: {item_quantity}\nItem ID: {item_ID}')  # add the content to the qrcode
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    img.save(f'product {item_ID}.png')  # saves the image as and .png file


def product_registration():  # register the product function
    global item_name, item_description, item_price, item_quantity, item_ID
    set_name()
    item_description = input('Type a description for the product (optional): ')
    set_price()
    set_quantity()
    set_ID()
    create_qr()


product_registration()

print(f'Item name: {item_name}\nItem description: {item_description}\nItem price: {item_price}\nItem quantity: '
      f'{item_quantity}\nItem ID: {item_ID}')
