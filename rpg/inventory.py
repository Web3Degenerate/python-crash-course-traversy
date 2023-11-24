# https://teamtreehouse.com/library/objectoriented-python-2/emulating-builtins

from items import Item

class Inventory:
    def __init__(self):
        self.slots = [] #create a list for inventory
        
    def add(self, item):
        self.slots.append(item) #add item to slots list
        
    #To use len function on object, must have __len__ function in object class
    #may want to limit number items a Character can store
    def __len__(self):
        return len(self.slots)

    #use built-in __contains__ method to check if an item is in inventory
    def __contains__(self, item):
        return item in self.slots

    # __iter__     #interates
    def __iter__(self):
        #yield similar to return, but doesn't exit method like return does. keeps going for all matches
        # for item in self.slots:
        #     yield item 
        #refactored: 
        yield from self.slots #python knows how to iterate through a list


    # __getitem__  #pluck with item or key
    
#__len__
coin = Item('coin', 'A gold coin')
inventory = Inventory()
inventory.add(coin)
print(len(inventory)) #returns 1

#__contains__
sword = Item('sword', 'sharp')
check_coin = coin in inventory
print(check_coin) #returns True
check_sword = sword in inventory
print(check_sword) #returns False

#__iter__
potion = Item('potion', 'freeze enemies for 5 seconds')
inventory.add(potion)
for item in inventory:
    print(item.description) #prints description for coin ('A gold coin') and potion ('freeze enemies for 5 seconds')


# Here is a class called Album that holds a list of songs. 
# Add an _iter_ method to our Album class and use yield or yield from so the songs in our album can be iterated through.
class Album:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __iter__(self):
        yield from self.songs



