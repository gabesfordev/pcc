guest_lst = ['alice', 'bob', 'clau', 'david', 'eli']
print(guest_lst)

print(f'{guest_lst[2].title()} is out.')

guest_lst.pop(2)
guest_lst.insert(2, 'zoro')
print(guest_lst)