from termcolor import colored, cprint
from Item import get_random_item, HpItem

STARTING_MAX_hp = 10
STARTING_GOLD = 0
STARTING_LOCATION = [0,0]

class Player:
    def __init__(self, path_to_save=None):
        self.inventory = []
        #testing
        for i in range(5):
            self.inventory.append(get_random_item())
        self.hp = STARTING_MAX_hp
        self.gold = STARTING_GOLD
        self.location = STARTING_LOCATION
        # if (path_to_save):
        #     self.load_from_save(path_to_save)

    def load_from_save(self, path_to_save):
        print('player: loading from save!')
    
    def move(self, tup):
        self.location[0] += tup[0]
        self.location[1] += tup[1]
    
    def print_inventory(self):
        print()
        for item in self.inventory:
            print(item)
        print()
    
    def print_info(self):
        print()
        print(colored("hp",'green') + f': {self.hp}')
        print(colored("gold",'yellow') + f': {self.gold}')
        print(colored("location",'blue') + f': {self.location}')
        print(f'{len(self.inventory)} item(s) in ' + colored("inventory",'cyan'))
        print()
    
    def index_item(self, item_name):
        for i in range(len(self.inventory)):
            if (self.inventory[i].name == item_name):
                return i
        return -1
    
    def heal(self, index):
        assert isinstance(self.inventory[index], HpItem), 'trying to heal with not hp item'
        item = self.inventory.pop(index)
        self.hp = min(10, self.hp + item.hp)
        print()
        if (self.hp == STARTING_MAX_hp):
            print(colored("hp",'green') + ' is now full at ' + str(self.hp))
        else:
            print(colored("hp",'green') + ' is now ' + str(self.hp))
        print()
    
    def use_utility(self, index):
        item = self.inventory[index]
        item.uses -= 1
        if (item.uses == 0):
            self.inventory.pop(index)