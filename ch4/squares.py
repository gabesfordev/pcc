squares = []

for value in list(range(1, 11)):
    square = value ** 2
    # print(f"{value} squared is equal to {square}")
    # print(f"adding {square} to squares")
    squares.append(square)
    # print('squares = ' + str(squares))

print(squares)