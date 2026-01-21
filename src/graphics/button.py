from core import Hitbox, Position, Camera
from .text import Text
from .ui_object import UiObject
import pygame


class Button(UiObject):
    def __init__(self, text: Text, position: Position, on_clicked=None,
                 size=(400, 100), color=(50, 50, 50), hover_color=(75, 75, 75)):
        super().__init__(position)
        self.text = text
        self.hitbox = Hitbox(self.get_global_position(), *size)
        self.color = color
        self.hover_color = hover_color
        self.on_clicked = on_clicked
        self._clicked = False
        self.center_text()

    # ===== UPDATE =====
    def update(self, delta, pg_event):
        # обновляем hitbox перед проверкой мыши
        self.hitbox.position = self.get_global_position()

        if not self.is_mouse_in_button():
            return

        for event in pg_event:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._clicked = True

        # hitbox тоже должен быть актуальным
        self.hitbox.position = self.get_global_position()

        if self._clicked:
            self._clicked = False
            if callable(self.on_clicked):
                self.on_clicked()

    def center_text(self):
        if self.text:
            self.text.center_in_hitbox(self.hitbox)

    def set_position(self, position: Position):
        self.position = position
        self.hitbox.position = self.get_global_position()
        self.center_text()

    def is_mouse_in_button(self):
        mouse_pos = Position(*pygame.mouse.get_pos())
        return self.hitbox.collides_point(mouse_pos)

    def center_by_x(self, screen_width: int):
        self.set_position(Position((screen_width - self.hitbox.width) / 2, self.position.y))

    # ===== RENDER =====
    def render(self, screen: pygame.Surface, camera: Camera | None = None):
        global_pos = self.get_global_position()
        draw_pos = camera.get_screen_position(global_pos) if camera else global_pos

        # обновляем hitbox и текст
        self.hitbox.position = global_pos

        surf = pygame.Surface((self.hitbox.width, self.hitbox.height))
        surf.fill(self.hover_color if self.is_mouse_in_button() else self.color)

        screen.blit(surf, draw_pos.to_tuple())

        if isinstance(self.text, Text):
            self.text.position = global_pos.copy()
            self.text.center_in_hitbox(self.hitbox)
            self.text.render(screen, camera)
