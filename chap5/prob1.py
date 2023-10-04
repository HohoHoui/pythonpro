
print('Your items:')


while True:
    item = input()
    if item in "\n":
        if item in "\n":
            break

tuItem = tuple(item)
print('\nPress the enter key to continue.')
print('You have ', len(tuItem), 'items in your possession.\n')

for 'healing potion' in tuItem:
    print('Press the enter key to continue.')
    print('You will live to fight another day.\n')

itemIndex = int(input('Enter the index number for an item in inventory:'))
print('At index', itemIndex, item(itemIndex))

a = input('Enter the index number to begin a slice:')
b = input('Enter the index number to end the slice:')
print('inventory[', a, ':', b, ']           ', "<'", realItem(int(a)), ", '", realItem(int(b)), "'>\n")

print('Press the enter key to continue.')
addItem = input('You find a chest.  It contatins:\n')

print('You add tne contents of the chest to your inventory.')
print('Your inventory is now:\n')

tu3 = realItem + addItem
print(tu3)

print('\nPress the enter key to exit.')
