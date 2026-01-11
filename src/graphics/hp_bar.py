from core import Position, Hitbox
import const


class HpBar:
    def __init__(self, position: Position, value: int, width=200, height=50,
                 fill_color = (0,255,0), background_color=(255, 0, 0), border_color = (100, 100, 100)):
        self.hitbox = Hitbox(position, width, height)
        self.value = value
        self.max_value = const.PLAYER_DEFAULT_MAX_HP
        self.fill_color = fill_color
        self.background_color = background_color
        self.border_color = border_color

    def set_max_value(self, max_value: int):
        self.max_value = max(1, max_value)
        self.value = min(self.value, self.max_value)

    def center_by_x(self, width):
        self.hitbox.position.x = width/2 - self.hitbox.width/2
    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
