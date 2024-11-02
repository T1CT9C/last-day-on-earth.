from config.Config import clear, line
from RPG.Ch import Character
from RPG.Entities import RadApple, RustyCannister, MRE, MedKit, Item, Map
import time

player = Character()
x,y = 0,0
#while True:
while True:
    clear()
    player.map.setToken(player, x, y)
    player.map.display()
    player.map.map1[x][y] = '.'
    # Get input for movement
    print("Enter W (up), A (left), S (down), D (right) or Q to quit:")
    move = input().upper()  # Convert input to uppercase to handle lowercase inputs

    # Move directly by modifying player.xpos and player.ypos
    if move == 'W' and x > 0:
        #player.xpos = x
        x -= 1
    elif move == 'S' and x < player.map.rows - 1:
        player.xpos = x
        x += 1
    elif move == 'A' and y > 0:
        player.ypos = y
        y -= 1
    elif move == 'D' and y < player.map.cols - 1:
        player.ypos = y
        y += 1
    elif move == 'Q':
        break  # Exit the game
    else:
        print("Invalid move! Please try again.")
        continue

    # Update the player position on the map
    clear()
    player.map.setToken(player, x, y)
    player.map.display()