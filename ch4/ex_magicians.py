#### INDEX      0       1      2
magicians = ['alice', 'bob', 'liz']

print("printing one by one.")
print('-' * 20)
print('[*] ' + magicians[0])
print('[*] ' + magicians[1])
print('[*] ' + magicians[2])

print('\nusing for loop:')
print('-' * 20)
for magician in magicians:
    # print('[*] ' + magician)
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')
    print("*" * 30)

print("Thank you everyone. That was great magic show!..")