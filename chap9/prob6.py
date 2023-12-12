class Critter:
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name

    def talk(self):
        print("Hi, I'm", self.name, "\n")

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if new_name == "":
            print("Critter's name can't be empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")
    
    name = property(get_name, set_name)

crit = Critter("Poochie")
crit.talk()

print("My critter's name is:", crit.get_name())

print()

print("Attempting to change my critter's name.")
crit.set_name("")

print()

print("Attempting to change my critter's name again.")
crit.set_name("Randolph")

print()

#print(crit.get_name())

print()

crit.talk()
