players = ['charls', 'martina', 'alice', 'bob', 'eli']

text = 'Here are the first three players in our list:'
print(text)
print('=' * len(text))

for player in players[:3]:
    print(f'[+] {player}')