guest_lst = ['alice', 'bob', 'clau', 'david', 'eli']
print(guest_lst)

print('Unfortunatly I can invite only two guests.\n')

popped_guest = guest_lst.pop()
print(f'{popped_guest} I\'m so sorry :(')

popped_guest = guest_lst.pop()
print(f'{popped_guest} I\'m so sorry :(')

popped_guest = guest_lst.pop()
print(f'{popped_guest} I\'m so sorry :(')

print(f'don\'t worry {guest_lst[0]}, your\'re still invited :)))')
print(f'don\'t worry {guest_lst[1]}, your\'re still invited :)))')

del guest_lst[0]
del guest_lst[0]
print(guest_lst)