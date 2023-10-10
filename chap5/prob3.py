import random

print('Guess the Word!!!')
print("In the game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")

words = ('difficult', 'banana', 'apple', 'python', 'daegue', 'catholic', 'university')
randWords = random.choice(words)
print('Length of the selected word:', len(randWords))
p#rint(randWords)

i = len(randWords)
#print('i : ', i)
guessedWords = ['_'] * len(randWords)

while i > 0:
    print('Remaining attempts:', i)
    print('Current guessed word:',guessedWords)

    answer = input('Guess a letter: ')
    
    if answer in randWords:
        for i in range(len(randWords)):
            if randWords[i] == answer:
                guessedWords[i] = answer
       # print(''.join(guessedWords))
    else:
        i -= 1
        print('Incorrect guess.')
    
    if '_' not in guessedWords:
        print('Congratulations! You guessed the word:', randWords)
        break
 
if '_' in guessedWords:
    print("You've uesd up all your attemps. The correcr word was", randWords)
