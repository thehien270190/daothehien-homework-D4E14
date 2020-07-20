from random import *
words = ['champion', 'meticulous', 'hexagon']
word = choice(words)
characters = list(word)
shuffle(characters)
for i in characters:
    print(i, end=' ')
print('\n')
answer = input('Your answer: ')
if answer == word:
    print('Hura')
else:
    print(':(')
