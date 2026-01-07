from .entity import Entity
from common import HpSystem
from common import const
from assets import Sound


class EntityPlayer(Entity):
    def __init__(self, world, spawn_point, creation_params: dict = None):
        super().__init__(world, spawn_point.copy(), 100, 100, creation_params)
        self.hp = HpSystem(const.PLAYER_DEFAULT_MAX_HP)
        self.god_mode = False
        self.spawn_point = spawn_point.copy()
        self.speed = 700

    def update(self, delta):
        if self.hp.is_dead:
            self.position = self.spawn_point.copy()
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
