import pygame
from core import Hitbox, Position
from .ui_object import UiObject


class Button(UiObject):
    def __init__(self, position: Position, size=(400, 100), on_clicked=None):
        super().__init__(position)

        self.hitbox = Hitbox(self.get_global_position(), *size)
        self.on_clicked = on_clicked

        self._hovered = False
        self._pressed = False
        self._enabled = True

    def update(self, delta, pg_events):
        if not self._enabled:
            self._hovered = False
            self._pressed = False
            return

        self.hitbox.position = self.get_global_position()
        mouse_pos = Position(*pygame.mouse.get_pos())

        self._hovered = self.hitbox.collides_point(mouse_pos)

        for event in pg_events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self._hovered:
                    self._pressed = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self._pressed:
                    self._pressed = False
                    if self._hovered and callable(self.on_clicked):
                        self.on_clicked()

    def is_hovered(self) -> bool:
        return self._hovered

    def is_pressed(self) -> bool:
        return self._pressed

    def set_enabled(self, value: bool):
        self._enabled = value
