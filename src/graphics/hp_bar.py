from core import Position, Hitbox, Camera
import const
import pygame
from .text import Text
from assets import Fonts


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

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera = None,
        text: str | None = None
    ):
        hp_bar_pos = camera.get_screen_position(self.position) if camera else self.position

        pygame.draw.rect(
            screen,
            self.background_color,
            (hp_bar_pos.x, hp_bar_pos.y, self.hitbox.width, self.hitbox.height)
        )

        fill_width = int(self.hitbox.width * (self.value / self.max_value))
        pygame.draw.rect(
            screen,
            self.fill_color,
            (hp_bar_pos.x, hp_bar_pos.y, fill_width, self.hitbox.height)
        )

        pygame.draw.rect(
            screen,
            self.border_color,
            (hp_bar_pos.x, hp_bar_pos.y, self.hitbox.width, self.hitbox.height),
            5
        )

        if text:
            text_obj = Text(
                text,
                Position(0, 0),
                Fonts.FONT_30
            )
            text_obj.center_in_hitbox(self.hitbox)
            text_obj.render(screen)
