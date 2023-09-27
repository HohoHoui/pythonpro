import random

heroHP = radom.randint(50, 100)
monsterHP = random.randint(50, 100)
count = 0

print('hero HP: ', heroHP, ', moster HP: ', mosterHP)

while(heroHP == 0 or mosterHP == 0):
    heroATK = ramdom.randint(-10, 20)
    mosterATK = random.randint(-10, 20)
    
    if(-10 <= heroATK and heroATK <= 0):
        print('hero(HP:', heroHP - mmosterATK, ', attak:', heroATK, ') fail <-> ', end='\n')
    elif(-10 <= mosterATK and monsterATK <= 0):
        print('moster(HP:', mosterHP - heroHP, ', attak:', mosterATK, ') fail')
    elif(0 <= heroATK ): 
        print('hero(HP:', heroHP - mmosterATK, ', attak:', heroATK, ') success <-> ', end='\n')
    elif(0 <= mosterATK):
        print('moster(HP:', mosterHP - heroHP, ', attak:', mosterATK, ') success')
    
    count += 1

print('\n-----------------------------------------------')
print('Total phase: ', count, ',')

if(heroHP == 0):
    print('Hero Win!!!!')
elif(mosterHP == 0):
    print('monster Win!!!!')

