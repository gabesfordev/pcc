pizza_original_list = ['pepperoni', '4 cheese', 'margherita']
friend_pizza = pizza_original_list[:]

# add new pizza to original list
pizza_original_list.append('neapolitan')
friend_pizza.append('sicilian')

text = 'My favorite pizzas are:'
print(text)
print('-' * len(text))
for pizza in pizza_original_list:
    print(f'[+] {pizza}')

print('=' * len(text))

text = '\nMy friends favorite pizzas are:'
print(text)
print('-' * len(text))
for pizza in friend_pizza:
    print(f'[+] {pizza}')

print('=' * len(text))