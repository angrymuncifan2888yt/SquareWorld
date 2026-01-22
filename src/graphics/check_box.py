from core import Camera
from .button import Button
import pygame


class CheckBox(Button):
    def __init__(
        self,
        position,
        on_clicked=None,
        size=(100, 100),
        color_off=(255, 0, 0),
        color_on=(0, 255, 0),
    ):
        super().__init__(position, size=size, on_clicked=self.toggle)

        self.is_on = False
        self._external_callback = on_clicked

        self.color_off = color_off
        self.color_on = color_on

    def toggle(self):
        self.is_on = not self.is_on
        if callable(self._external_callback):
            self._external_callback()

    # ===== RENDER =====
    def render(self, screen: pygame.Surface, camera: Camera | None = None):
        global_pos = self.get_global_position()
        draw_pos = camera.get_screen_position(global_pos) if camera else global_pos

        self.hitbox.position = global_pos

        color = self.color_on if self.is_on else self.color_off

        surf = pygame.Surface((self.hitbox.width, self.hitbox.height))
        surf.fill(color)
        screen.blit(surf, draw_pos.to_tuple())
