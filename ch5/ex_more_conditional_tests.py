string = 'What a wonderful day today.'
car = 'BMW'
age = 18
names = ['alice', 'bob', 'charles', 'tim', 'marie']

# Tests for equality and inequality with strings
print('\nTests for equality and inequality with strings')
print(string == 'What a wonderful day today.')
print(string == 'What a wonderful day today')

# Tests using the lower() function
print('\nTests using the lower() function')
print('BMW' == car)
print('bmw' == car)
print('bmw' == car.lower())

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
print("\nNumerical test")
print(age == 5)
print(18 != age)
print(age > 5)
print(30 < age)
print(age >= 5)
print(30 <= age)


# Tests using the and keyword and the or keyword
print('\nTests using the and keyword and the or keyword')
print(age == 18 and car == 'BMW')
print(age == 18 and car == 'audi')
print(age == 18 or car == 'audi')

# Test whether an item is in a list
print('\nTest whether an item is in a list')
print('bob' in names)
print('liz' in names)

# Test whether an item is not in a list
print('\nTest whether an item is not in a list')
print('bob' not in names)
print('liz' not in names)