import random

words = ["about", "absolutely", "advice", "against", "allow", "animal", "announce", "answer", "approach", "arrange", "arrive", "attend", "balance", "beautiful", "believe", "benefit", "boil", "bright", "bring", "choose", "clothes"]

randWords = list(random.choice(words))
count = 0

while True:
    answer = input("Enter your guess: ")
    
    if answer in randWords:
        print("Yes!", answer, "is in the word!")
        
    else:
        print(answer, "is not exist")
        count += 1
    
    if count == 0:
        print("------")
        print("|   |")
        print("|     ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("------------")
    
    if count == 1:
        print("------")
        print("|   |")
        print("|   o")
        print("|    ")
        print("|")
        print("|")
        print("|")
        print("------------")
    if count == 2:
        print("------")
        print("|   |")
        print("|   o")
        print("|  -+-")
        print("|   |")
        print("|    ")
        print("|")
        print("-----------")
    if count == 3:
        print("-----")
        print("|   |")
        print("|   o")
        print("|  -+-")
        print("|   |")
        print("|   /\\")
        print("\nthe end")
        break
    print("You've used the following letters: ")
    print(randWords)
    print("\nSo far, the word is:")
    leng = ['_'] *len(randWords)
    
    for i in range(len(randWords)):
        if randWords[i] == answer:
            leng[i] += answer
    print(''.join(leng))

    if '_' not in leng:
        break;
