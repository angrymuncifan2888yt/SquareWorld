from core import Hitbox



class Block:
    def __init__(self, position, max_hardness):
        self.hitbox = Hitbox(position, 100, 100)
        self.max_hardness = max_hardness
        self.hardness = max_hardness
        self.alive = True

    def update(self, delta: float):
        if self.hardness <= 0:
            self.alive = False
            
    def damage(self, amount=1):
        self.hardness -= amount

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
