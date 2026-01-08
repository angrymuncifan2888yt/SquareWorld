from .entity import Entity
from common import HpSystem
from common import const
from assets import Sound


class EntityPlayer(Entity):
    def __init__(self, world, spawn_point, creation_params: dict = None):
        super().__init__(world, spawn_point.copy(), 100, 100,creation_params)
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
            Sound.DAMAGE.play_once()
    
    def add_hp(self, hp):
        self.hp.add_hp(hp)
        Sound.HEAL.play_once()
        
    def kill(self):
        if not self.god_mode:
            self.hp.kill()
            Sound.DAMAGE.play_once()
            
    def onBlockCollision(self, block):
        if not self.god_mode:
            self.hitbox.handle_collision(block.hitbox)

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb

    def stop_sound(self):
        Sound.DAMAGE.stop()
        Sound.HEAL.stop()
