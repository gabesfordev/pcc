""" 
4-5. Summing a Million:
        
    Make a list of the numbers from one to one million,
    and then use min() and max() to make sure your list actually starts at one and
    ends at one million. Also, use the sum() function to see how quickly Python can
    add a million numbers.
"""

lst = []

for num in list(range(1000001)):
    lst.append(num)

print('The lowest number in our list is {}'.format(min(lst)))
print(f'The highest number in our list is {max(lst)}')
print('The sum of all numbers from our list is ', sum(lst))