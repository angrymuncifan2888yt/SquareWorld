from core import Timer, Hitbox


class TextCursor:
    def __init__(self, position):
        self.hitbox = Hitbox(position, 10, 40)
        self.blink_timer = Timer(0.4)
        self.is_visible = True
        self.current_symbol = 0

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value

    def update(self, delta: float):
        self.blink_timer.update(delta)
        if self.blink_timer.finished:
            self.is_visible = not self.is_visible
            self.blink_timer.reset()
