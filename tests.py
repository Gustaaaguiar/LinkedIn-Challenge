# add users with password to be able to add products
# half done

# add a system to sell the items and automatically calculate the final price and remove the right quantity of the
# spreadsheet

import secrets


# register the user:

user = str(input('Insert the username: '))
regis = int(input('You want to:\n1-Use your password \n2-Use an auto generated password '))

if regis == 1:
    password = str(input('Insert the password: '))
elif regis == 2:
    special_char = '!@#$%&*-+?'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    alphabet = letters + letters.upper() + special_char + numbers
    password = ''.join(secrets.choice(alphabet) for i in range(10))  # generate password with the number of
    # digits I want
    print(f'Your password is: {password}')
else:
    print('please select a valid answer')
