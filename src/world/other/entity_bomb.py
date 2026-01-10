from ..entity import Entity
from core import Timer, Hitbox, Position
from graphics import Text
from .entity_player import EntityPlayer
from ..block.entity_block import EntityBlock
from assets import Fonts, SoundStorage, calculate_sound_volume, AdvancedSound


class EntityBomb(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        # Initialize the bomb entity with size 75x75
        super().__init__(world, position, 75, 75, creation_params)

        # Timers for bomb behavior
        self.defuse_timer = Timer(10)  # Time before bomb automatically explodes
        self.explosion_timer = Timer(0.3)  # Duration of the explosion effect
        self.damage_timer = Timer(0.3)  # Timer controlling damage intervals
        self.is_exploding = False  # Flag indicating if bomb is currently exploding
        self.can_damage = False  # Flag indicating if bomb can currently deal damage

        # Override default timers if provided in creation_params
        if isinstance(creation_params, dict):
            if creation_params.get("defuse_time"):
                self.defuse_timer = Timer(creation_params["defuse_time"])
            if creation_params.get("explosion_time"):
                self.explosion_timer = Timer(creation_params["explosion_time"])
            if creation_params.get("damage_timer"):
                self.damage_timer = Timer(creation_params.get("damage_timer"))
        
        # Initialize explosion sound
        self.explosion_sound = AdvancedSound(SoundStorage.EXPLOSION)

    def explode(self):
        # Start explosion: enlarge hitbox and enable damage
        self.is_exploding = True

        # Calculate new hitbox centered on original position
        center_x = self.hitbox.position.x + self.hitbox.width // 2
        center_y = self.hitbox.position.y + self.hitbox.height // 2

        new_width = 200
        new_height = 200

        new_x = center_x - new_width // 2
        new_y = center_y - new_height // 2

        self.hitbox = Hitbox(Position(new_x, new_y), new_width, new_height)

        self.damage_timer.reset()
        self.can_damage = True

        # Play explosion sound with volume based on distance to player
        self.explosion_sound.play_once(calculate_sound_volume(self.position, self.world.player.position, 1500))

    def onBlockCollision(self, block):
        # Handle collision with blocks only if not exploding
        if not self.is_exploding:
            super().onBlockCollision(block)

    def onEntityCollision(self, entity):
        # Handle collision with entities
        if self.is_exploding:
            entity.onBombExplosionCollision(self)  # Apply explosion effect

        if isinstance(entity, EntityPlayer):
            # Deal damage to player if explosion allows it
            if self.can_damage:
                entity.damage(200)
                self.can_damage = False

    def update(self, delta: float):
        if not self.is_exploding:
            # Update defuse countdown
            self.defuse_timer.update(delta)

            # Trigger explosion if timer finishes
            if self.defuse_timer.finished:
                self.explode()
        else:
            # Update timers for explosion duration and damage intervals
            self.explosion_timer.update(delta)
            self.damage_timer.update(delta)

            # Control damage intervals during explosion
            if self.can_damage and self.damage_timer.finished:
                self.can_damage = True
            elif not self.can_damage and self.damage_timer.finished:
                self.damage_timer.reset()
                self.can_damage = True

            # Destroy bomb entity when explosion finishes
            if self.explosion_timer.finished:
                self.destroy()

    def onBombExplosionCollision(self, bomb):
        # Bombs are immune to other bombs
        pass

    def stop_sound(self):
        # Stop the explosion sound if playing
        self.explosion_sound.stop()
