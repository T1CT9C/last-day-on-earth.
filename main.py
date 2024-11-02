from config.Config import clear, line
from RPG.Ch import Character
from RPG.Entities import RadApple, RustyCannister, MRE, MedKit, Item, Map

player = Character()
while True:
    clear()
    player.map.setToken(player, player.xpos, player.ypos, player.token)
    player.map.display()
    x = int(input())
    if x == 1: 
        player.xpos += 1
    elif x == 2:
        player.ypos += 1