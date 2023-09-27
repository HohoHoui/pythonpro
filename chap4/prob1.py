import random

print('I sense your energy. Your true emotions are coming across my screen.')
print('You are...')

mood = random.randint(1, 11)

if(7 <= mood and mood <= 10):
    print('------------')
    print('|   0   0  |')
    print('|     <    | ')
    print('|  .     . |')
    print('|   .   .  | ')
    print('|     ..   |')
    print('------------')
elif( 4 <= mood and mood <= 6 ):
    print('-------------')
    print('|   0   0   |')
    print('|     <     |')
    print('|           |')
    print('|           |')
    print('|   .....   |')
    print('-------------')
elif(1<= mood and mood <= 3):
    print('-------------')
    print('|   0   0   |')
    print('|     <     |')
    print('|    ....   |')
    print('|   .    .  |')
    print('-------------')

print('\n...today.')
print('\nPress the enter key to quit.')

