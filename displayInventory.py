stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}
inventory = dict()

def displayInventory(inventory):
    index = 0
    print ("Inventory:")
    for item in inventory:
        items = list(inventory.keys())
        quantityItems = list(inventory.values())
        print (quantityItems[index], items[index])
        index = index + 1
    

        


displayInventory(stuff)