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
    
    def battle(self, target, atktype, gib):  #melee attack, spell maybe pokemon
        match atktype: 
            case 1:         #Normal melee attack (weapon also)
                damage = (self.Atk + self.Weapon.atk) * 10
                finaldmg = damage // target.Def
                target.hp -= finaldmg
                return finaldmg if gib is True else None
            case 2:
                ...
                # add spell or pokemon type smth here
                # maybe item use

class Enemy:
    def __init__(self, player, type, typedict, names):
        self.name = random.choice(names)

        self.Hp = random.randint(0, player.lvl // 2) + player.lvl.getcurrent()
        self.atk = random.randint(0,type[type]['atk']) + player.lvl.getcurrent()
        self.Def = random.randint(0,type[type]['def']) + player.lvl.getcurrent()
        
        self.xpdrop = random.randint(player.lvl.getcurrent() // 2, player.lvl.getcurrent()) * player.lvl.getcurrent()
    
    def AttackPlayer(self, player, gib):
        damage = (self.atk + random.randint(0, player.lvl.getcurrent())) * 10
        finaldmg = damage // player.Def
        player.hp.deCurrent(finaldmg)
        return finaldmg if gib is True else None