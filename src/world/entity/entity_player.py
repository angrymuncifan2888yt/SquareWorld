from .entity import Entity
from common import HpSystem
from common import const
from assets import Sound


class EntityPlayer(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        super().__init__(world, position, 100, 100, creation_params)
        self.hp = HpSystem(const.PLAYER_DEFAULT_MAX_HP)
        self.god_mode = False

    def update(self, delta):
        if self.hp.is_dead:
            self.position.x = 0
            self.position.y = 0
            self.hp.revive()

    def damage(self, hp):
        if not self.god_mode:
            self.hp.damage(hp)
            Sound.damage()
    
    def add_hp(self, hp):
        self.hp.add_hp(hp)
        Sound.heal()
        
    def kill(self):
        if not self.god_mode:
            self.hp.kill()
            Sound.damage()
            
    def onBlockCollision(self, block):
        if not self.god_mode:
            self.hitbox.handle_collision(block.hitbox)
