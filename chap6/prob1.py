realItem = tuple()
print("Your Item:")
Item = [ 'sword', 'armor', 'shield', 'healing potion' ]

for i in Item:
    print(i)

print('\nPress the enter key to continue.')
while True:
    enter = input()
    if enter == '':
        break
print('You have ', len(Item), 'items in your possession.\n')

for i in Item:
    if 'healing potion' in i:
        print('Press the enter key to continue.')
        print('You will live to fight another day.')

itemIndex = int(input('\nEnter the index number for an item in inventory: '))
print('At index', itemIndex,"is",  Item[itemIndex])

a = int(input('\nEnter the index number to begin a slice: '))
b = int(input('Enter the index number to end the slice: '))
print('inventory[', a, ':', b, ']           ', Item[a:b], "\n")

print('Press the enter key to continue.')
while True:
    enter = input()
    if enter == '':
        break

Chest = []
Chest = input('You find a chest.  It contatins:\n').split(",")

print('You add tne contents of the chest to your inventory.')
print('Your inventory is now:')
Item  = Item + Chest
print(Item)

if 'sword' in Item:
    print('\nPress the enter key to continue.')
    while True:
        enter = input()
        if enter == '':
            break
    print('You trande your sowrd for a crossbow.')
    print('Your inventory is now:')
    for i in Item:
        if 'sword' in i:
            index = Item.index(i)
            Item[index] = 'crossbow'

print(Item)

if 'gold' and 'gems' in Item:
    print('\nPress the enter key to continue.')
    while True:
        enter = input()
        if enter == '':
            break
    print('You use your gold and gems to buy an orb of future telling.')
    print('Your inventory is now:')
    for i in Item:
        if 'gold' in i:
            index = Item.index('gold')
            del Item[index]
    for i in Item:
        if 'gems' in i:
            index = Item.index('gems')
            del Item[index]
    Item.append('orb of future telling')
    print(Item)

if 'shield' in Item:
    print('\nPress the enter key to continue.')
    while True:
        enter = input()
        if enter == '':
            break
    print('In a great battle, your shield is destroyed.')
    print('Your inventory is now:')
    for i in Item:
        if 'shield' in i:
            index = Item.index('shield')
            del Item[index]
    print(Item)

if 'crossbow' and 'armor' in Item:
    print('\nPress the enter key to continue.')
    while True:
        enter = input()
        if enter == '':
            break
    print('Your crossbow and armor stolen by thieves.')
    print('Your inventory is now:')
    for i in Item:
        if 'crossbow' in i:
            index = Item.index('crossbow')
            del Item[index]
    for i in Item:
        if 'armor' in i:
            index = Item.index('armor')
            del Item[index]
    print(Item)

print('\n\nPress the enter key to exit.')

