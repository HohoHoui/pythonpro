import random

heroHP = random.randint(50, 100)
monsterHP = random.randint(50, 100)
count = 0

print('hero HP:', heroHP, ', moster HP:', monsterHP)

while heroHP > 0 and monsterHP > 0:
    heroATK = random.randint(-10, 20)
    monsterATK = random.randint(-10, 20)
    
   
    if (-10 <= heroATK and heroATK <= 0) and (-10 <= monsterATK and monsterATK <= 0):
        print('hero(HP:',heroHP, ', attck:',heroATK, ') fail <->', end=' ')
        print('monster(HP:',monsterHP,', attck:',monsterATK, ') fail')
    elif (0 < heroATK) and (-10 <= monsterATK and monsterATK <= 0):
        monsterHP -= heroATK
        print('hero(HP:',heroHP, ', attck:',heroATK, ') success <->', end=' ')
        if(monsterHP <= 0):
            print('moster(HP:',monsterHP, ', attck:',monsterATK, ') fail', end=' ')
        else: 
            print('monster(HP:',monsterHP, ', attck:',monsterATK, ') fail')
    elif (-10 <= heroATK and heroATK <= 0) and (0 < monsterATK):
        heroHP -= monsterATK
        print('hero(HP:',heroHP, ', attck:',heroATK, ') fail <->', end=' ')
        print('monster(HP:',monsterHP, ', attck:',monsterATK, ') success')
    elif (0 < heroATK) and (0 < monsterATK):
        heroHP -= monsterATK
        monsterHP -= heroATK
        print('hero(HP:',heroHP, ', attck:',heroATK, ') success <->', end=' ')
        if(monsterHP <= 0):
            print('moster(HP:',monsterHP, ', attck:',monsterATK, ') success', end=' ')
        else:
            print('moster(HP:',monsterHP, ', attck:',monsterATK, ') success')
    
    count += 1

print('\n-----------------------------------------------')
print('Total phase:', count, ',')

if heroHP > 0:
    print('Hero Win!!!!')
elif monsterHP > 0:
    print('monster Win!!!!')

