geek = { 
        "404" : "clueless.", 
        "Uninstalled" : "being fired.  Especially popular during the dot-bomb era."
    }

while True:
    print("\n\tGeek Translator\n")
    print("\t0 - Quit")
    print("\t1 - Look Up a Geek Term")
    print("\t2 - Add a Geek Term")
    print("\t3 - Redefine a Geek Term")
    print("\t4 - Delete a Geek Term\n")

    choice = int(input("Choice: "))
    
    if choice == 0:
        break
    elif choice == 1:
        lookUp = input("\nWhat term do you want me to translate?:" )
        
        if lookUp in geek:
            print("\n", lookUp, "means", geek[lookUp])
        else:
            print("\nI have no idea what", lookUp, "is.")
    elif choice == 2:
        addName = input("What is geek name? : ")
        addExplain = input("What is geek explain? : ")
        geek[addName] = addExplain
    elif choice == 3:
        redefine = input("What is geek name? : ")
        if redefine in geek:
            reExplain = input("What would you change the description to? : ")
            geek[redefine] = reExplain
        else:
            print(redefine, "is not exist")
    elif choice == 4:
        delName  = input("What is geek name? : ")
        if delName in geek:
            del geek[delName]
        else:
            print(delName, "is not exist")

