menu = ('pizza', 'pasta', 'steak')
print("\nThis is original menu:")
for i in menu:
    print(i)

# menu[0] = 'hot dog' # this will return TypeError

print("\nThis is modified menu:")
menu = ('burger', 'wings', 'stake')
for i in menu:
    print(i)