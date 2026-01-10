from ..entity import Entity
from ..components import HasHealth, BombImmune
from assets import SoundStorage
import const


class EntityPlayer(BombImmune, Entity, HasHealth):
    def __init__(self, world, spawn_point, creation_params: dict = None):
        # Initialize the player entity with size 100x100 at spawn point
        super().__init__(world, spawn_point.copy(), 100, 100, creation_params)
        self.hp = 100
        self.max_hp = const.PLAYER_DEFAULT_MAX_HP

        self.god_mode = False  # Flag for invincibility
        self.spawn_point = spawn_point.copy()  # Keep a copy of the spawn position for respawn
        self.speed = 700  # Movement speed of the player

    def on_death(self):
        # Respawn player at spawn point if dead
        self.position = self.spawn_point.copy()
        self.revive()
        SoundStorage.DAMAGE.play()

    def damage(self, amount):
        super().damage(amount)
        SoundStorage.DAMAGE.play()

    def kill(self):
        # Instantly kill the player if not in god mode
        if not self.god_mode:
            super().kill()
            
    def heal(self, amount):
        super().heal(amount)
        SoundStorage.HEAL.play()

    def onBlockCollision(self, block):
        # Handle collision with a block unless in god mode
        if not self.god_mode:
            self.hitbox.handle_collision(block.hitbox)
