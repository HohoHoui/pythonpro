class Critter:
    """A virtual per"""
    def __init__(self):
        print("A new critter has been born!")
    def talk(self):
        print("Hi. I'm an instance of class Critter.")

crit1 = Critter()
crit2 = Critter()

print()

crit1.talk()
print()
crit2.talk()

print()

while True:
    ans = input("Press the enter key ot exit.")
    if ans == '':
        break
