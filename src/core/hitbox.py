from .position import Position


class Hitbox:
    def __init__(self, position: Position, width: int, height: int):
        self.__position = position
        self.__width = width
        self.__height = height
    
    def collides_hitbox(self, hitbox: "Hitbox") -> bool:
        return not (
            self.position.x + self.width < hitbox.position.x or
            self.position.x > hitbox.position.x + hitbox.width or
            self.position.y + self.height < hitbox.position.y or
            self.position.y > hitbox.position.y + hitbox.height
        )

    def collides_point(self, point_position: Position, camera: "Camera" = None) -> bool:
        if camera:
            screen_pos = camera.get_screen_position(self.position)
        else:
            screen_pos = self.position

        return (screen_pos.x <= point_position.x <= screen_pos.x + self.width and
                screen_pos.y <= point_position.y <= screen_pos.y + self.height)

    def handle_collision(self, hitbox: "Hitbox"):
        if not self.collides_hitbox(hitbox):
            return

        dx1 = hitbox.position.x + hitbox.width - self.position.x
        dx2 = self.position.x + self.width - hitbox.position.x
        dy1 = hitbox.position.y + hitbox.height - self.position.y
        dy2 = self.position.y + self.height - hitbox.position.y

        overlap_x = dx1 if dx1 < dx2 else -dx2
        overlap_y = dy1 if dy1 < dy2 else -dy2

        if abs(overlap_x) < abs(overlap_y):
            self.position.x += overlap_x
        else:
            self.position.y += overlap_y

    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, value: Position):
        self.__position = value

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int):
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int):
        self.__height = value
