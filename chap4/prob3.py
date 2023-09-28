import random

randnum = random.randint(1, 100)
count = 0

guessnum = None

print("         Welcome to 'Guess My Number'!\n")
print("I'm thinking of a number between 1 and 100.")
print('Try to guess it in as few attemps as possible.\n')

while(randnum != guessnum):
    guessnum = int(input('Take a guess: '))
    if(randnum > guessnum):
        print('Higher...')
    elif(randnum < guessnum):
        print('Lower...')
    count+=1

print('You guessed it! The number was', randnum)
print('And it only took you', count, 'tries!\n\n\n')

print('Press the enter key to quit.')

