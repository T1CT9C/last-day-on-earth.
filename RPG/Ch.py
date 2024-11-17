from RPG.Entities import Map, PointSystem, Effects
from RPG.data import deviltypehash
import random

class Character:
    def __init__(self, subclass, name, Weapon ):
        # implement this later
        self.Hp = PointSystem(50, 50, min = 0)
        self.subclass = subclass['name']
        self.name = name
        
        self.Weapon = Weapon
        self.WeaponName = Weapon['name']
        self.summon = devil(deviltypehash, 'Light', 'Light Devil')
        self.effects = Effects()
        
        self.Atk = random.randint(0,10) + subclass['atk']
        self.Def = random.randint(0,10) + subclass['def']
        self.Spd = random.randint(0,10) + subclass['spd']
        self.Luk = random.randint(0,20)

        self.lvl = PointSystem(100, 10, min = 0)
        self.exp = PointSystem(10, 0)

        self.RadCoins = PointSystem(1000, 100, min = 0) # currency
        self.Food = PointSystem(20,20, min = 0) # used for moving in dungeon
        
        self.xpos = 0
        self.ypos = 0
        
        self.token = '\033[32m' + 'P' + '\033[39m'
        self.map = Map()
    
    def battle(self, target, atktype, gib):  #melee attack, spell maybe pokemon
        match atktype: 
            case 1:         #Normal melee attack (weapon also)
                damage = (self.Atk + self.Weapon['atk']) * 7
                damage += random.randint(0,10)
                finaldmg = damage // target.Def
                target.Hp -= finaldmg
                return finaldmg if gib is True else None
            case 2:
                ...
                # add spell or pokemon type smth here
                # maybe item use

class Enemy:
    def __init__(self, player, enemytype, type, typedict, names):
        self.name = random.choice(names)
        self.type = type
        self.effects = Effects()
        
        self.Hp = random.randint(0, player.lvl.getcurrent() // 2) + player.Hp.getcurrent()
        self.MaxHp = random.randint(0, player.lvl.getcurrent() // 2) + player.Hp.getcurrent()
        self.atk = random.randint(0,enemytype[type]['atk']) + player.lvl.getcurrent()
        self.Def = random.randint(0,enemytype[type]['def']) + player.lvl.getcurrent()
        
        self.xpdrop = random.randint(player.lvl.getcurrent() // 2, player.lvl.getcurrent()) * player.lvl.getcurrent()
    
    def AttackPlayer(self, player, gib):
        damage = (self.atk + random.randint(0, player.lvl.getcurrent())) * 5
        finaldmg = damage // player.Def
        player.Hp.decCurrent(finaldmg)
        return finaldmg if gib is True else None
    
    def SetHp(self): self.Hp = self.MaxHp #some bug is therw fix it

#Pokemon
class devil:
    def __init__(self, deviltype, type, name):
        self.devil = deviltypehash[type]

        self.name = name
        self.Hp = self.devil['Hp']
        self.lvl = PointSystem(100,self.devil['level'])
        self.type = self.devil['type']
        
        self.atkSpell = self.devil['attack']
        self.defSpell = self.devil['defense']
        self.mana = PointSystem(100, 100) # uses different mana for every spell
        
        def GetType(self): return self.type
        def GetName(self): return self.name