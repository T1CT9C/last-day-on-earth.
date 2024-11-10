import random
from RPG.Ch import Character, Enemy
from RPG.Entities import EnemyToken
from config.Config import clear, line
import time

class Game:
    def __init__(self):
        ...
        
    def move(self, player, y, x, etoken):
        while True:
            clear()
            player.map.setToken(player, y, x)
            player.map.setToken(etoken, etoken.ypos, etoken.xpos)
            player.map.display()
            player.map.map1[etoken.ypos][etoken.xpos] = player.map.copy1[etoken.ypos][etoken.xpos]
            player.map.map1[y][x] = player.map.copy1[y][x]
            # Get input for movement
            print("Enter W (up), A (left), S (down), D (right) or Q to quit:")
            move = input().upper()  # Convert input to uppercase to handle lowercase inputs
        
            # Move directly by modifying player.xpos and player.ypos
            if move == 'W' and y > 0:
                y -= 1
                player.ypos = y
            elif move == 'S' and y < player.map.rows - 1:
                y += 1
                player.ypos = y
            elif move == 'A' and x > 0:
                x -= 1
                player.xpos = x
            elif move == 'D' and x < player.map.cols - 1:
                x += 1
                player.xpos = x
            elif move == '' or ' ':
                ...
            elif move == 'Q':
                break  # Exit the game
            else:
                print("Invalid move! Please try again.")
                continue
        
            # Update the player position on the map
            clear()
            player.map.setToken(player, y, x)

            if etoken.xpos < x + 3 and etoken.ypos < y + 3:
                if etoken.xpos > x and (etoken.xpos - 1 <= len(player.map.map1[0]) - 1):
                    etoken.xpos -= 1
                elif etoken.xpos < x and (etoken.xpos + 1 >= 0):
                    etoken.xpos += 1
    
                if etoken.ypos > y and (etoken.ypos - 1 <= len(player.map.map1) - 1):
                    etoken.ypos -= 1
                elif etoken.ypos < y and (etoken.ypos + 1 >= 0):
                    etoken.ypos += 1
            else:
                if random.randint(0,1) == 1:
                    etoken.ypos = etoken.ypos + 1 if etoken.ypos + 1 <= len(player.map.map1) else etoken.ypos
                    etoken.xpos = etoken.xpos + 1 if etoken.xpos + 1 <= len(player.map.map1[1]) else etoken.xpos
                else:
                    etoken.ypos = etoken.ypos - 1 if etoken.ypos - 1 > 0 else etoken.ypos
                    etoken.xpos = etoken.xpos - 1 if etoken.xpos - 1 > 0 else etoken.xpos
            player.map.setToken(etoken, etoken.ypos, etoken.xpos)
            
            if x == etoken.xpos and y == etoken.ypos: 
                self.battle(player)
                time.sleep(0.6)
                etoken.xpos = random.randint(-6,6)
                etoken.ypos = random.randint(-6, 6)
                player.map.setToken(etoken, etoken.ypos, etoken.xpos)
                player.map.setToken(player, y, x)
            
            player.map.display()
            print(player.xpos, player.ypos)
            time.sleep(1)
            
            # Enemy movement
            
    
        
    def run(self):
        s = {'name': 'cleric', 'atk':5, 'def':6, 'spd':6}
        w = {'name': 'baseball bat', 'atk': 5}
        player = Character(s, 'oof', w)
        Etoken = EnemyToken(random.randint(0, len(player.map.map1) + 1), random.randint(0, len(player.map.map1) + 1))
        x = 0
        y = 0  # add some way to input player current loc
        self.move(player, y, x, Etoken)
    
    def battle(self, player):
        clear()
        # Sample data for enemy attributes
        enemytype = {
            'orc': {'atk': 10, 'def': 5},
            'goblin': {'atk': 5, 'def': 2},
            'troll': {'atk': 15, 'def': 10}
        }

        # Sample data for type-specific characteristics
        typedict = {
            'orc': {'weakness': 'fire', 'strength': 'earth'},
            'goblin': {'weakness': 'light', 'strength': 'dark'},
            'troll': {'weakness': 'ice', 'strength': 'earth'}
        }

        # List of possible names for enemies
        names = ['Goruk', 'Blitz', 'Zagroth', 'Snarl', 'Grimm']
        
        type = 'orc'  # or 'goblin', 'troll'
        enemy = Enemy(player, enemytype, type, typedict, names)
        
        player.Hp.setCurrent(player.Hp.getmax())
        enemy.SetHp()
        
        while True:
            clear()
            line('Battle')
            print('Enemy')
            print(f'Name: {enemy.name}, Type: {enemy.type},  HP: {enemy.Hp}, Atk: {enemy.atk}, Def: {enemy.Def}')
            line('------')
            print('Player')
            print(f'Name: {player.name}, HP: {player.Hp.getcurrent()}, Atk: {player.Atk}, Def: {player.Def}')
            line('------')
            print()
            print(
"""
(1) to attack 
(2) to block
(3) to use item
(4) to flee
""")
            while True:
                try:
                    choice = int(input())
                    break
                except ValueError:
                    print('Wrong Input')
            
            match choice:
                # this is for attack (normal)
                case 1: #add different choices here to use weapon, spell smth like tht
                    playerdamage = player.battle(enemy, 1, True)
                    print(f'You dealt {playerdamage} damage to {enemy.name}')
                    if enemy.Hp <= 0:
                        print(f'You Succesfully defeated {enemy.name}!')
                        break
               
                # this is to flee
                case 4:
                    clear()
                    print(f'You successfully fled from {enemy.name}!')
                    # add some random thing here to see if u can flee
                    time.sleep(2)
                    return
                    
            enemydamage = enemy.AttackPlayer(player,True)
            print(f'You take {enemydamage} from {enemy.name}')
            if player.Hp.getcurrent() <= 0:
                print('YOU DIE NOOB')
                break
            print('Press (enter) to proceed')
            input()            