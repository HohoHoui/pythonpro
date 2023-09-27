import random

heroHP = random.randint(50, 100)
monsterHP = random.randint(50, 100)
count = 0

print('hero HP: ', heroHP, ', moster HP: ', monsterHP)

while heroHP != 0 or monsterHP != 0:
    heroATK = random.randint(-10, 20)
    monsterATK = random.randint(-10, 20)
    
    if -10 <= heroATK and heroATK <= 0:
        print('hero(HP:', heroHP - monsterATK, ', attak:', heroATK, ') fail <-> ', end=' ')
    elif 0 <= heroATK:
        print('hero(HP:', heroHP - monsterATK, ', attak:', heroATK, ') success <-> ', end=' ')
    
    if -10 <= monsterATK and monsterATK <= 0:
        print('moster(HP:', monsterHP - heroATK, ', attak:', monsterATK, ') fail')
    elif 0 <= monsterATK:
        print('moster(HP:', monsterHP - heroATK, ', attak:', monsterATK, ') success')
    
    count += 1

print('\n-----------------------------------------------')
print('Total phase: ', count, ',')

if heroHP == 0:
    print('Hero Win!!!!')
elif monsterHP == 0:
    print('monster Win!!!!')

