capital_cities = ['tbilisi', 'paris', 'london', 'berlin', 'madrid']

# print first three items in the list
print('\nThe first three items in the list are:\n')
for item in capital_cities[:3]:
    print(f'[+] {item.title()}')

# print three items from the middle of the list
print('\nThree items from the middle of the list are:\n')
for item in capital_cities[1:4]:
    print(f'[+] {item.title()}')

# print last three items of the list
print('\nThe last tree items of the list are:\n')
for item in capital_cities[-3:]:
    print(f'[+] {item.title()}')