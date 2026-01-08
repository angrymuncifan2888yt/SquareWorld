from .entity import Entity
from core import Timer, Hitbox, Position
from graphics import Text
from .entity_player import EntityPlayer
from assets import Fonts, SoundStorage, calculate_sound_volume, AdvancedSound


class EntityBomb(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        super().__init__(world, position, 75, 75, creation_params)

        self.defuse_timer = Timer(10)
        self.explosion_timer = Timer(0.3)  # длительность взрыва
        self.damage_timer = Timer(0.3)
        self.is_exploding = False
        self.can_damage = False

        self.text_timer = Text(str(self.defuse_timer.time_left), Position(0, 0), Fonts.FONT_30)
        self.text_timer.center_in_hitbox(self.hitbox)

        if isinstance(creation_params, dict):
            if creation_params.get("defuse_time"):
                self.defuse_timer = Timer(creation_params["defuse_time"])
            if creation_params.get("explosion_time"):
                self.explosion_timer = Timer(creation_params["explosion_time"])
            if creation_params.get("damage_timer"):
                self.damage_timer = Timer(creation_params.get("damage_timer"))
        
        self.explosion_sound = AdvancedSound(SoundStorage.EXPLOSION)

    def explode(self):
        self.is_exploding = True

        center_x = self.hitbox.position.x + self.hitbox.width // 2
        center_y = self.hitbox.position.y + self.hitbox.height // 2

        new_width = 200
        new_height = 200

        new_x = center_x - new_width // 2
        new_y = center_y - new_height // 2

        self.hitbox = Hitbox(Position(new_x, new_y), new_width, new_height)

        self.damage_timer.reset()
        self.can_damage = True

        self.explosion_sound.play_once(calculate_sound_volume(self.position, self.world.player.position, 1500))

    def onBlockCollision(self, block):
        if not self.is_exploding:
            super().onBlockCollision(block)

        elif self.can_damage:
            block.damage(2)
            self.can_damage = False

    def onEntityCollision(self, entity):
        if self.is_exploding:
            entity.onBombExplosionCollision(self)

        if isinstance(entity, EntityPlayer):
            if self.can_damage:
                entity.damage(200)
                self.can_damage = False

    def update(self, delta: float):
        if not self.is_exploding:
            self.defuse_timer.update(delta)
            self.text_timer.text = str(round(self.defuse_timer.time_left, 1))
            self.text_timer.center_in_hitbox(self.hitbox)

            if self.defuse_timer.finished:
                self.explode()
        else:
            self.explosion_timer.update(delta)
            self.damage_timer.update(delta)

            if self.can_damage and self.damage_timer.finished:
                self.can_damage = True
            elif not self.can_damage and self.damage_timer.finished:
                self.damage_timer.reset()
                self.can_damage = True

            if self.explosion_timer.finished:
                self.destroy()

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb

    def stop_sound(self):
        self.explosion_sound.stop()
