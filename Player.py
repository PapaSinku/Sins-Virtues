from termcolor import colored, cprint
from Item import get_random_item, HpItem, Fist, CoinItem
STARTING_MAX_hp = 10
STARTING_GOLD = 0
STARTING_LOCATION = [0,0]
STARTING_EQIPPED_ITEM = Fist()

class Player:
    def __init__(self, path_to_save=None):
        self.inventory = []
        #testing
        self.max_hp = STARTING_MAX_hp
        self.hp = self.max_hp
        self.coin = STARTING_GOLD
        self.location = STARTING_LOCATION
        self.equipped = STARTING_EQIPPED_ITEM
        for i in range(5):
            self.add_item(get_random_item())
        # if (path_to_save):
        #     self.load_from_save(path_to_save)

    def load_from_save(self, path_to_save):
        print('player: loading from save!')
    
    def move(self, tup):
        self.location[0] += tup[0]
        self.location[1] += tup[1]
    
    def print_inventory(self):
        for item in self.inventory:
            print(item)
    
    def print_info(self):
        print(colored("hp",'green') + f': {self.hp}')
        print(colored("coins",'yellow') + f': {self.coin}')
        print(colored("location",'blue') + f': {self.location}')
        print(f'{len(self.inventory)} item(s) in ' + colored("inventory",'cyan'))
    
    def index_item(self, item_name):
        for i in range(len(self.inventory)):
            if (self.inventory[i].name == item_name):
                return i
        return -1
    
    def heal(self, index):
        assert isinstance(self.inventory[index], HpItem), 'trying to heal with not hp item'
        item = self.inventory.pop(index)
        self.hp = min(10, self.hp + item.hp)
        if (self.hp == self.max_hp):
            print(colored("hp",'green') + ' is now full at ' + str(self.hp))
        else:
            print(colored("hp",'green') + ' is now ' + str(self.hp))
    
    def use_utility(self, index):
        item = self.inventory[index]
        item.uses -= 1
        if (item.uses == 0):
            self.inventory.pop(index)
    
    def add_item(self, item):
        if (isinstance(item, CoinItem)):
            self.coin += item.amount
            return
        self.inventory.append(item)
    
    def refill_hp(self):
        self.hp = self.max_hp
    
    def equip_item(self, item):
        self.equipped = item
    
    def use_steroid(self, index):
        STEROID_ADD = 5
        self.max_hp += STEROID_ADD
        self.hp = self.max_hp
    
    def sell(self, index):
        price = self.inventory[index].get_sell_price()
        self.coin += price
        self.inventory.pop(index)
        return price