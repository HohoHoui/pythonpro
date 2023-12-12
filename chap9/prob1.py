class Critter:
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm an instance of class Critter.")


crit = Critter()
crit.talk()

print()

while True:
    ans = input("Press the enter key to exit.")
    if ans == '':
        break
