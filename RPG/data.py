import random

# Air devil
def airsmash(enemy):
    damage = 10 + random.randint(1,5)
    enemy.Hp.decCurrent(damage)
    enemy.effects.isWounded = True
    return f"Your devil uses air smash, succesfully dealing {damage} damage to {enemy.name}, wounding them!"

def earthquake(enemy):
    damage = 5 + random.randint(5, 10)
    enemy.Hp.decCurrent(damage)
    enemy.effects.isBleeding = True
    return f"Earth Devil uses Earthquake, dealing {damage} damage to {enemy.name}, wounding them!"

def fireblast(enemy):
    damage = 10 + random.randint(1, 10)
    enemy.Hp.decCurrent(damage)
    enemy.effects.isBurned = True
    return f"Fire Devil uses Fireblast, dealing {damage} damage and burning {enemy.name}!"

def tsunami(enemy):
    damage = 12 + random.randint(5, 10)
    enemy.Hp.decCurrent(damage)
    enemy.effects.isSoaked = True
    return f"Water Devil uses Tsunami, dealing {damage} damage and soaking {enemy.name}!"

def lightsmite(enemy):
    damage = 18 + random.randint(2, 8)
    enemy.Hp.decCurrent(damage)
    return f"Light Devil uses Light Smite, dealing {damage} damage to {enemy.name}!"

def darkcurse(enemy):
    damage = 20 + random.randint(5, 10)
    enemy.Hp.decCurrent(damage)
    enemy.effects.isCursed = True
    return f"Dark Devil uses Dark Curse, dealing {damage} damage and cursing {enemy.name}!"

# Define defenses
def airbarrier(player):
    player.Def += int( player.Def * 0.5)
    return "Air Devil summons a barrier of wind, increasing defense 50% for one turn!"

def stonewall(player):
    player.effects.isInvincible = True
    return "Earth Devil creates a stone wall, nullifying one attack!"

def fireshield(player):
    player.effects.FireArmor = True
    return "Fire Devil generates a shield of flames, damaging any attackers for 5 damage!"

def watercloak(player):
    player.Def += int( player.Def * 0.75)
    return "Water Devil surrounds itself in water, reducing damage from attacks by 75%!"

def lightscreen(player):
    player.effects.reflectDamage = True
    return "Light Devil creates a screen of light, reflecting 100% of the damage back to the attacker!"

def darkveil(player):
    player.effects.isInvisible = True
    return "Dark Devil shrouds itself in shadows, making itself and you invisiblee!"

airdevil = {
    'type': 'Sky',
    'Hp': 20,
    'level': 1,
    'attack': [airsmash],
    'defense': [airbarrier]
}
earthdevil = {
    'type': 'Earth',
    'Hp': 50,
    'level': 1,
    'attack': [earthquake],
    'defense': [stonewall]
}
firedevil = {
    'type': 'Fire',
    'Hp': 25,
    'level': 1,
    'attack': [fireblast],
    'defense': [fireshield]
}
waterdevil = {
    'type': 'Water',
    'Hp': 30,
    'level': 1,
    'attack': [tsunami],
    'defense': [watercloak]
}
lightdevil = {
    'type': 'Light',
    'Hp': 40,
    'level': 1,
    'attack': [lightsmite],
    'defense': [lightscreen]
}
darkdevil = {
    'type': 'Dark',
    'Hp': 40,
    'level': 1,
    'attack': [darkcurse],
    'defense': [darkveil]
}

deviltypehash = {
    'air': airdevil,
    'earth': earthdevil,
    'fire': firedevil,
    'water': waterdevil,
    'light': lightdevil,
    'dark': darkdevil,
}

#enemy 
enemytype = {
    'orc': {'atk': 10, 'def': 5},
    'goblin': {'atk': 5, 'def': 2},
    'troll': {'atk': 15, 'def': 10}
}


typedict = {
    'orc': {'weakness': 'fire', 'strength': 'earth'},
    'goblin': {'weakness': 'light', 'strength': 'dark'},
    'troll': {'weakness': 'ice', 'strength': 'earth'}
}

# List of possible names for enemies
names = ['Goruk', 'Blitz', 'Zagroth', 'Snarl', 'Grimm']

type = random.choice(['goblin', 'orc', 'troll'])