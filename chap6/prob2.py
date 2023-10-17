score = [('Moe', 1000), ('Larry', 1500), ('Curly', 3000)]
while True:
    print('\tHigh Scores Keeper\n')
    print('\t0 - Quit')
    print('\t1 - List Scores')
    print('\t2 - Add a Score\n')

    choice = int(input('Choice: '))
    
    if choice == 0:
        break
    if choice == 1:
        print('\nHigh Score\n')
        print('NAME\tSCORE')
        
        score.sort(key = lambda x: (-x[1], x[0]))
        
        for x, y in score:
            print(x, "\t", y)
    if choice == 2:
        addPerson = input("What is the player's name?: ")
        addScore = int(input("What score did the player get?: "))
        score.append((addPerson, addScore))
