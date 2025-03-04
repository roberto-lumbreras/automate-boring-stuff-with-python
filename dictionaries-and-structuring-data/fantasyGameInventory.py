def displayInventory(inventory):
    print('Inventory:')
    numberOfItems = 0
    for k, v in inventory.items():
        print(str(v)+" "+k)
        numberOfItems+=int(v)
    print('Total number of items: '+str(numberOfItems))
inventory = {'apple': '3', 'stick': '1', 'rock': '0', 'potion': '5'}
displayInventory(inventory)
def addToInventory(inventory, itemList):
    for item in itemList:
        inventory.setdefault(item,0)
        inventory[item] = str(int(inventory[item])+1)
dragonLoot = ['dragon claw', 'dragon claw', 'dragon fang', 'potion']
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
    