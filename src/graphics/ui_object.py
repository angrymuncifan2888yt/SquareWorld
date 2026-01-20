from core import Position


class UiObject:
    def __init__(self, position: Position | tuple):
        if isinstance(position, tuple):
            self.position = Position(*position)
        else:
            self.position = position

        self.parent = None

    def get_global_position(self) -> Position:
        pos = self.position.copy()
        if self.parent:
            parent_pos = self.parent.get_global_position()
            pos.x += parent_pos.x
            pos.y += parent_pos.y
        return pos

    def input(self, delta, pg_event):
        pass

    def update(self, delta, pg_event):
        pass

    def render(self, screen, camera=None):
        pass

    def center_by_x(self, width: int):
        self.position.x = width / 2

    def center_by_y(self, height: int):
        self.position.y = height / 2
