from core import Hitbox
from common import const



class Block:
    def __init__(self, world, position, max_hardness):
        self.hitbox = Hitbox(position, *const.BLOCK_SIZE)
        self.max_hardness = max_hardness
        self.hardness = max_hardness
        self.world = world

    @classmethod
    def texture(cls):
        return

    def update(self, delta: float):
        if self.hardness <= 0:
            self.world.remove_block(self)
            
    def damage(self, amount=1):
        self.hardness -= amount

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
