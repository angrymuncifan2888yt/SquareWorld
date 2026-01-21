from core import Position, Camera
from .ui_object import UiObject
import pygame


class Text(UiObject):
    def __init__(
        self,
        text: str,
        position: Position,
        font: pygame.font.Font,
        color: tuple[int, int, int] = (255, 255, 255)
    ):
        super().__init__(position)

        self.text = text
        self.font = font
        self.color = color

    def center_by_x(self, screen_width: int):
        text_width = self.font.size(self.text)[0]
        self.position.x = (screen_width - text_width) / 2

    def center_in_hitbox(self, hitbox):
        w, h = self.font.size(self.text)
        self.position.x = hitbox.position.x + (hitbox.width - w) / 2
        self.position.y = hitbox.position.y + (hitbox.height - h) / 2

    # ===== RENDER =====
    def render(
        self,
        surface: pygame.Surface,
        camera: Camera | None = None
    ):
        global_pos = self.get_global_position()
        draw_pos = camera.get_screen_position(global_pos) if camera else global_pos

        text_surface = self.font.render(
            self.text,
            True,
            self.color
        )

        surface.blit(text_surface, draw_pos.to_tuple())
