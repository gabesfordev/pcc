my_food = ['pizza', 'pasta', 'lasagna']
friend_food = my_food[:]

my_food.append('cheesecake')
friend_food.append('ice cream')

print('=' * 30)
print('My favorite food:\n')
for food in my_food:
    print(f'[*] {food}')

print('=' * 30)
print('My favorite food:\n')
for food in friend_food:
    print(f'[*] {food}')