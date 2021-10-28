requested_toppings = ['mushrooms', 'green pappers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pappers':
        print('Sorry, we are out of green papers right now.')
    else:
        print('Adding ' + requested_topping + '.')


print('\nFinnished making your pizza!')