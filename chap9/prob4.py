class Critter:
    total = 0

    def __init__(self, name):
        Critter.total += 1
        print("A critter has been born!")

    @staticmethod
    def status():
        print("The total number of critters is", Critter.total)

print("Accessing the class attribute Critter.totla:", Critter.total)

print()

print("Creating critters.")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

print()
Critter.status()

print()
print("Accessing the class attribute through an object:", crit1.total)

print()

while True:
    ans = input("Press the enter key to exit.")
    if ans == '':
        break
