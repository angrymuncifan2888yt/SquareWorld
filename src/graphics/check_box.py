from .button import Button
from core import Hitbox, Position
import pygame


class CheckBox:
    def __init__(self, position, on_clicked=None, size=(100, 100)):
        self.hitbox = Hitbox(position, *size)
        self.button = Button(None, self.position, (self.hitbox.width, self.hitbox.height))
        self.is_on = False
        self.on_clicked = on_clicked

    def update(self, pg_event):
        if self.button.isClicked(pg_event):
            self.is_on = not self.is_on

            if callable(self.on_clicked):
                self.on_clicked()

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
        self.button.position = value

    def center_by_x(self, screen_width: int):
        self.position = Position((screen_width - self.hitbox.width) / 2, self.position.y)

    def render(self, screen: pygame.Surface, camera=None):
        pos = camera.get_screen_position(self.position) if camera else self.position
        surf = pygame.Surface((self.hitbox.width, self.hitbox.height))
        color = (0, 255, 0) if self.is_on else (255, 0, 0)
        surf.fill(color)
        screen.blit(surf, pos.to_tuple())
