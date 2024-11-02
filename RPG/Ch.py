from RPG.Entities import Map

class Character:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.token = 'P'
        self.map = Map()