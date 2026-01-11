from .button import Button
from core import Hitbox, Position


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
