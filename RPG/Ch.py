from RPG.Entities import Map, PointSystem
import random

class Character:
    def __init__(self, subclass, name, Weapon ):
        # implement this later
        self.Hp = PointSystem(1000, 50, min = 0)
        self.subclass = subclass['name']
        self.name = name
        self.Weapon = Weapon
        
        self.Atk = random.randint(0,10) + subclass['atk']
        self.Def = random.randint(0,10) + subclass['def']
        self.Spd = random.randint(0,10) + subclass['spd']
        self.Luk = random.randint(0,20)

        self.lvl = PointSystem(100, 1, min = 0)
        self.exp = PointSystem(10, 0)

        self.RadCoins = PointSystem(1000, 100, min = 0) # currency
        self.Food = PointSystem(20,20, min = 0) # used for moving in dungeon
        
        self.xpos = 0
        self.ypos = 0
        
        self.token = 'P'
        self.map = Map()