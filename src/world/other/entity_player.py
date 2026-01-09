from ..entity import Entity
from common import HpSystem
from common import const
from assets import SoundStorage


class EntityPlayer(Entity):
    def __init__(self, world, spawn_point, creation_params: dict = None):
        # Initialize the player entity with size 100x100 at spawn point
        super().__init__(world, spawn_point.copy(), 100, 100, creation_params)
        self.hp = HpSystem(const.PLAYER_DEFAULT_MAX_HP)  # Player's health system
        self.god_mode = False  # Flag for invincibility
        self.spawn_point = spawn_point.copy()  # Keep a copy of the spawn position for respawn
        self.speed = 700  # Movement speed of the player

    def update(self, delta):
        # Respawn player at spawn point if dead
        if self.hp.is_dead:
            self.position = self.spawn_point.copy()
            self.hp.revive()

    def damage(self, hp):
        # Reduce HP if not in god mode and play damage sound
        if not self.god_mode:
            self.hp.damage(hp)
            SoundStorage.DAMAGE.play()
    
    def add_hp(self, hp):
        # Heal the player and play heal sound
        self.hp.add_hp(hp)
        SoundStorage.HEAL.play()
        
    def kill(self):
        # Instantly kill the player if not in god mode
        if not self.god_mode:
            self.hp.kill()
            SoundStorage.DAMAGE.play()
            
    def onBlockCollision(self, block):
        # Handle collision with a block unless in god mode
        if not self.god_mode:
            self.hitbox.handle_collision(block.hitbox)

    def onBombExplosionCollision(self, bomb):
        # Player is immune to bomb explosions
        pass
