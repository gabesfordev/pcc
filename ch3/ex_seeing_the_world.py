# Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['dubai', 'ghana', 'canada', 'egypt', 'france']

# Print your list in its original order.
print("Original:")
print(locations)

# Use sorted() to print your list in alphabetical order
# without modifieng the actual list
print("\nSorted:")
print(sorted(locations))

# check if original list is unchanged
print("\nOriginal:")
print(locations)

# Use sorted() to print the list in reverse alphabetical order.
print("\nReversed:")
print(sorted(locations, reverse=True))

# check if original list is unchanged
print("\nOriginal:")
print(locations)

# Use reverse() to change the order of your list.
print("\nReversed:")
locations.reverse()
print(locations)

# Use reverse() to change the order of your list again.
print("\nReversed (again):")
locations.reverse()
print(locations)

# Use sort() to change your list so it’s stored in alphabetical order.
print("\nSort:")
locations.sort()
print(locations)

# Use sort() to change your list so it’s stored in reverse alphabetical order.
print("\nSort (reversed):")
locations.sort(reverse=True)
print(locations)