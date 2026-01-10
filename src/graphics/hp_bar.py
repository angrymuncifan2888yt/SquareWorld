from core import Position, Hitbox
from .text import Text
from assets import Fonts
import const


class HpBar:
    def __init__(self, position: Position, value: int):
        self.hitbox = Hitbox(position, 200, 50)
        self.__value = value
        self.max_value = const.PLAYER_DEFAULT_MAX_HP
        self.text = Text(str(self.value), Position(0, 0), Fonts.FONT_30)
        self.text.center_in_hitbox(self.hitbox)

    def set_max_value(self, max_value: int):
        self.max_value = max(1, max_value)
        self.value = min(self.value, self.max_value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value2):
        self.__value = value2
        self.text.text = str(value2)
        self.text.center_in_hitbox(self.hitbox)

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
