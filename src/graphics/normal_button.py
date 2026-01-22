from core import Camera
from .text import Text
from .button import Button
import pygame


class NormalButton(Button):
    def __init__(
        self,
        text: Text,
        position,
        on_clicked=None,
        size=(400, 100),
        color=(50, 50, 50),
        hover_color=(75, 75, 75),
        pressed_color=(30, 30, 30),
    ):
        super().__init__(position, size=size, on_clicked=on_clicked)

        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color

        self.center_text()

    def center_text(self):
        if self.text:
            self.text.center_in_hitbox(self.hitbox)

    def center_by_x(self, screen_width: int):
        new_x = (screen_width - self.hitbox.width) / 2
        self.position.x = new_x
        self.hitbox.position = self.get_global_position()
        self.center_text()

    # ===== RENDER =====
    def render(self, screen: pygame.Surface, camera: Camera | None = None):
        global_pos = self.get_global_position()
        draw_pos = camera.get_screen_position(global_pos) if camera else global_pos

        self.hitbox.position = global_pos

        if self.is_pressed():
            color = self.pressed_color
        elif self.is_hovered():
            color = self.hover_color
        else:
            color = self.color

        surf = pygame.Surface((self.hitbox.width, self.hitbox.height))
        surf.fill(color)
        screen.blit(surf, draw_pos.to_tuple())

        if self.text:
            self.text.position = global_pos.copy()
            self.text.center_in_hitbox(self.hitbox)
            self.text.render(screen, camera)
