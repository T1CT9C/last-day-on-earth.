class Item:   
    def __init__(self, name, type, subtype, incMain, incSub, ispermanent, isconsumable):
        self.name = name
        self.type = type
        self.subtype = subtype
        self.incMain = incMain
        self.incSub = incSub
    
        self.ispermanent = ispermanent
        self.isconsumable = isinstance
    
    def get_name(self): return self.name
    def get_type(self): return self.type
    def get_subtype(self): return self.subtype
    def get_incMain(self): return self.incMain
    def get_incSub(self): return self.incSub
    def is_permanent(self): return self.ispermanent
    def is_consumable(self): return self.isconsumable

class Map:
    def __init__(self, token='P'): 
        
        self.map1 = [
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."], ]

        self.copy1 = [
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."],
            [".",".",".",".",".",".","."], ]
        
        self.rows = len(self.map1)
        self.cols = len(self.map1[0])
        self.startchar = "."

    def display(self):
        print('+' + ''.join('-' * 1 for _ in range(self.cols * 4 + 3)) + '+')
        print('|' + ''.join(' ' * 1 for _ in range(self.cols * 3 + 10)) + '|')
        
        for row in range(self.rows):
            print('|   ', end='')
            for col in range(self.cols):
                print(self.map1[row][col],end="   |   ") if col is self.cols-1 else print(self.map1[row][col],end="   ")
            print()
            if row is not (self.rows - 1):
                print('|' + ''.join(' ' * 1 for _ in range(self.cols * 3 + 10)) + '|')
        
        print('|' + ''.join(' ' * 1 for _ in range(self.cols * 3 + 10)) + '|')
        print('+' + ''.join('-' * 1 for _ in range(self.cols * 4  + 3)) + '+')

    def getrows(self): return self.rows
    def getcols(self): return self.cols
    
    def setToken(self, player, yindex, xindex):
        self.map1[player.ypos][player.xpos] = self.copy1[player.ypos][player.xpos]
        self.map1[yindex][xindex] = player.token
    

class PointSystem:
    def __init__(self, max, current, min = 0):
        self.max = max
        self.current = current if current < self.max else self.max
        self.min = min if min else 0
        
    # Getters
    def getmax(self): return self.max
    def getmin(self): return self.min
    def getcurrent(self): return self.current

    # Setters
    def setMax(self, newmax): self.max = newmax
    def setMin(self, newmin): self.min = newmin if newmin > 0 else 0
    
    def setCurrent(self, newCurrent): 
        self.current= newCurrent if newCurrent <= self.max and newCurrent > self.min else self.current
    def decCurrent(self, dec): self.current = self.min if dec > self.current else self.current - dec
    def incCurrent(self, inc): 
        self.current = self.max if inc > self.max or inc + self.current > self.max else self.current + inc

class EnemyToken:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.token = '\033[31m' + 'E' + '\033[39m'
    
# Items
RadApple =       Item('Irradiated apple', 'Inc Food', 'Inc Rad', 5, 15, False, True)
RustyCannister = Item('Rusty Canister', 'Inc Food', 'Inc Rad', 25, 5, False, True)
MRE =            Item('MRE', 'Inc Food', 'Inc HP', 50, 25, False, True)
MedKit =         Item('MedKit', 'Inc HP', 'Heal Bleeding', 100, True, False, True)