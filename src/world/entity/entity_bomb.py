from .entity import Entity
from core import Timer, Hitbox, Position
from graphics import Text
from assets import Fonts


class EntityBomb(Entity):
    def __init__(self, position, creation_params: dict = None):
        super().__init__(position, 75, 75, creation_params)

        self.defuse_timer = Timer(10)
        self.explosion_timer = Timer(0.3)
        self.is_exploding = False
        self.text_timer = Text(str(self.defuse_timer.time_left), Position(0, 0), Fonts.FONT_30)
        self.text_timer.center_in_hitbox(self.hitbox)

        if isinstance(creation_params, dict):
            if creation_params.get("defuse_time"):
                self.defuse_timer = Timer(creation_params["defuse_time"])

            if creation_params.get("explosion_time"):
                self.explosion_timer = Timer(creation_params["explosion_time"])

    def explode(self):
        self.is_exploding = True

        old_hitbox = self.hitbox

        center_x = old_hitbox.position.x + old_hitbox.width // 2
        center_y = old_hitbox.position.y + old_hitbox.height // 2

        new_width = 200
        new_height = 200

        new_x = center_x - new_width // 2
        new_y = center_y - new_height // 2

        self.hitbox = Hitbox(
            Position(new_x, new_y),
            new_width,
            new_height
        )

    def update(self, delta: float):
        if not self.is_exploding:
            self.defuse_timer.update(delta)
            self.text_timer.text = str(round(self.defuse_timer.time_left, 1))
            self.text_timer.center_in_hitbox(self.hitbox)

            if self.defuse_timer.finished:
                self.explode()

        elif self.is_exploding:
            self.explosion_timer.update(delta)

            if self.explosion_timer.finished:
                self.alive = False
