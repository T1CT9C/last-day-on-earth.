class Item:
    
    def __init__(self, name, type, subtype, incMain, incSub, ispermanent, isconsumable):
        self.name = name
        self.type = type
        self.subtype = subtype
        self.incMain = incMain
        self.incSub = incSub
    
        self.ispermanent = ispermanent
        self.isconsumable = False
        
    
    def get_name(self): return self.name
    def get_type(self): return self.type
    def get_subtype(self): return self.subtype
    def get_incMain(self): return self.incMain
    def get_incSub(self): return self.incSub
    def is_permanent(self): return self.ispermanent
    def is_consumable(self): return self.isconsumable

# Items
RadApple =       Item('Irradiated apple', 'Inc Food', 'Inc Rad', 5, 15, False, True)
RustyCannister = Item('Rusty Canister', 'Inc Food', 'Inc Rad', 25, 5, False, True)
MRE =            Item('MRE', 'Inc Food', 'Inc HP', 50, 25, False, True)
MedKit =         Item('MedKit', 'Inc HP', 'Heal Bleeding', 100, True, False, True)

class Map:
    def __init__(self): 
        
        self.map1 = [
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."], ]
        
        self.rows = len(self.map1)
        self.cols = len(self.map1[0])

    def display(self):
        print('+' + ''.join('-' * 1 for _ in range(self.cols * 4 + 3)) + '+')
        print('|' + ''.join(' ' * 1 for _ in range(self.cols * 3 + 10)) + '|')
        
        for row in range(self.rows):
            print('|   ', end='')
            for col in range(self.cols):
                print(self.map1[row][col],end="   |   ") if col is self.cols - 1 else print(self.map1[row][col],end="   ")
            print()
            if row is not (self.rows - 1):
                print('|' + ''.join(' ' * 1 for _ in range(self.cols * 3 + 10)) + '|')
        
        print('|' + ''.join(' ' * 1 for _ in range(self.cols * 3 + 10)) + '|')
        print('+' + ''.join('-' * 1 for _ in range(self.cols * 4  + 3)) + '+')

    def getrows(self): return self.rows
    def getcols(self): return self.cols