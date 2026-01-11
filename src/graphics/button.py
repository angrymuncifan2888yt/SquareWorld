from core import Hitbox, Position
from .text import Text
import pygame


class Button:
    def __init__(self, text: Text, position: Position, size=(400, 100),
                 color=(50, 50, 50), hover_color=(75, 75, 75)):
        self.text = text
        self.hitbox = Hitbox(position, *size)
        self.color = color
        self.hover_color = hover_color
        
        self.center_text()
    def center_text(self):
        if self.text:
            self.text.center_in_hitbox(self.hitbox)
    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value

    def set_position(self, position):
        self.position = position
        self.center_text()

    def is_mouse_in_button(self):
        if self.hitbox.collides_point(Position(*pygame.mouse.get_pos())):
            return True

        return False

    def isClicked(self, pg_event):
        if self.is_mouse_in_button():
            for event in pg_event:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return True
                return False
        return False

    def center_by_x(self, screen_width: int):
        self.set_position(Position((screen_width - self.hitbox.width) / 2, self.position.y))
