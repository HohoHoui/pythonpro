import random

print('Welcome to Word Jumble!')
print('Unscramble the letters to make a word.')

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
randWords = random.choice(words)
listWords = list(randWords)
shuffle = random.shuffle(listWords)
shuffleWords = ''.join(s for s in listWords)

#print('ran', randWords)
#print('list', listWords)
#print('shuffle', shuffleWords)

print('Jumbled word:', shuffleWords)
answer = input('Your guess: ')

if answer == randWords:
    print("awesome, that's correct. The word was:", randWords)
else:
    print("Sorry, that's no correct. The word was:", randWords)
