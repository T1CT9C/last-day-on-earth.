from RPG.Entities import Map, PointSystem

class Character:
    def __init__(self, subclass, name, Weapon,  ):
        # implement this later
        self.Atk = 0
        self.Def = 0
        self.Spd = 0
        self.Luk = 0

        self.lvl = PointSystem(100, 1, min = 0)
        self.exp = PointSystem(10, 0)

        self.RadCoins = PointSystem(1000, 100, min = 0) # currency
        self.Food = PointSystem(20,20, min = 0) # used for moving in dungeon
        
        self.xpos = 0
        self.ypos = 0
        
        self.token = 'P'
        self.map = Map()