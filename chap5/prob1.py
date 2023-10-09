realItem = tuple()
print("Your Item:")
#Item = input().split('\n')
while True:
    Item = input()
    if Item  ==  "":
        if realItem:
            break
    else:
        realItem += (Item,) 

print(realItem)
print('\nPress the enter key to continue.')
print('You have ', len(realItem), 'items in your possession.\n')

for i in realItem:
    if 'healing potion' in i:
        print('Press the enter key to continue.')
        print('You will live to fight another day.')

itemIndex = int(input('\nEnter the index number for an item in inventory: '))
print('At index', itemIndex,"is",  realItem[itemIndex])

a = int(input('\nEnter the index number to begin a slice: '))
b = int(input('Enter the index number to end the slice: '))
print('inventory[', a, ':', b, ']           ', realItem[a:b], "\n")

print('Press the enter key to continue.')

Chest = tuple()
Chest = input('You find a chest.  It contatins:\n').split(",")

print('You add tne contents of the chest to your inventory.')
print('Your inventory is now:')

tu3 = realItem +tuple(Chest)
print(tu3)

print('\n\nPress the enter key to exit.')
