from RPG.Ch import Character
from config.Config import clear

class Game:
    def __init__(self):
        ...
   
    def run(self):
        s = {'name': 'cleric', 'atk':5, 'def':6, 'spd':6}
        player = Character(s, 'oof', 'baseball bat')
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
                x -= 1
                player.xpos = x
            elif move == 'S' and x < player.map.rows - 1:
                x += 1
                player.xpos = x
            elif move == 'A' and y > 0:
                y -= 1
                player.ypos = y
            elif move == 'D' and y < player.map.cols - 1:
                y += 1
                player.ypos = y
            elif move == 'Q':
                break  # Exit the game
            else:
                print("Invalid move! Please try again.")
                continue
        
            # Update the player position on the map
            clear()
            player.map.setToken(player, x, y)
            player.map.display()
            print(player.xpos, player.ypos)
            input()