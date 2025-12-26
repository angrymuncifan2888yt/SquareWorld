import math


class Vec2:
    def __init__(self, direction: float = 0.0):
        self.__direction = direction % 360

    @property
    def direction(self) -> float:
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        self.__direction = value % 360

    @property
    def x(self) -> float:
        rad = math.radians(self.__direction)
        return math.cos(rad)

    @property
    def y(self) -> float:
        rad = math.radians(self.__direction)
        return -math.sin(rad)

    def set_angle(self, direction: float):
        self.direction = direction

    def __str__(self):
        return f"Vector2(x={self.x:.2f}, y={self.y:.2f}, angle={self.direction})"
