import random


def product_registration():
    item_name = input('Type the product name: ')

    item_description = input('Type a description for the product (optional): ')

    item_price = float(input('Type the price of the product: '))

    item_quantity = int(input('Type the quantity to be sold: '))

    ID = ''

    for i in range(5):
        number = random.randint(0, 9)
        ID += str(number)
    item_ID = f'#{ID}'



# print(f'Item name: {item_name}\nItem description: {item_description}\nItem price: {item_price}\nItem quantity: '
#       f'{item_quantity}\nItem ID: {item_ID}')
