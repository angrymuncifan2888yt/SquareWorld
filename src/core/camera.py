from dataclasses import dataclass
from .position import Position


@dataclass
class Camera:
    position: Position
    width: int
    height: int

    def get_screen_position(self, position: Position) -> Position:
        return Position(position.x - self.position.x, position.y - self.position.y)

    def center_on(self, target_position: Position, target_width: float, target_height: float):
        center_x = target_position.x + target_width / 2
        center_y = target_position.y + target_height / 2

        self.position.x = center_x - self.width / 2
        self.position.y = center_y - self.height / 2
