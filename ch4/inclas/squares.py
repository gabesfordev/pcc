squares = []

for number in range(1, 11):
    square = number ** 2
    squares.append(square)

print(squares)

# list comprehension
squares = [number ** 2 for number in range(1, 11)]
print(squares)