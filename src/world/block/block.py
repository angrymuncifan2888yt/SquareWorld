from core import Hitbox



class Block:
    def __init__(self, position):
        self.hitbox = Hitbox(position, 100, 100)

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
