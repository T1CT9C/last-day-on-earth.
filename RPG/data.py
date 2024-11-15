import random

# devil
airdevil = {
    'type': 'Sky',
    'Hp': 20,
    'level': 1,
    'attack': [],
    'defense': []
}
earthdevil = {
    'type': 'Earth',
    'Hp': 50,
    'level': 1,
    'attack': [],
    'defense': []
}
firedevil = {
    'type': 'Fire',
    'Hp': 25,
    'level': 1,
    'attack': [],
    'defense': []
}
waterdevil = {
    'type': 'Water',
    'Hp': 30,
    'level': 1,
    'attack': [],
    'defense': []
}
lightdevil = {
    'type': 'Light',
    'Hp': 40,
    'level': 1,
    'attack': [],
    'defense': []
}
darkdevil = {
    'type': 'Dark',
    'Hp': 40,
    'level': 1,
    'attack': [],
    'defense': []
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