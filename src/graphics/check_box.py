from core import Hitbox, Position, Camera
from .ui_object import UiObject
from .button import Button
import pygame


class CheckBox(UiObject):
    def __init__(
        self,
        position: Position,
        on_clicked=None,
        size=(100, 100)
    ):
        super().__init__(position)

        self.hitbox = Hitbox(self.position, *size)
        self.is_on = False
        self.on_clicked = on_clicked

        self.button = Button(
            text=None,
            position=Position(0, 0),
            on_clicked=self.toggle,
            size=size
        )
        self.button.parent = self

    def toggle(self):
        self.is_on = not self.is_on
        if callable(self.on_clicked):
            self.on_clicked()

    # ===== INPUT =====
    def input(self, delta, pg_event):
        self.button.input(delta, pg_event)

    # ===== UPDATE =====
    def update(self, delta, pg_event):
        self.button.update(delta, pg_event)

    # ===== RENDER =====
    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None
    ):
        global_pos = self.get_global_position()
        draw_pos = camera.get_screen_position(global_pos) if camera else global_pos

        self.hitbox.position = global_pos

        surf = pygame.Surface((self.hitbox.width, self.hitbox.height))
        surf.fill((0, 255, 0) if self.is_on else (255, 0, 0))
        screen.blit(surf, draw_pos.to_tuple())

        print(self.button.position)
        # self.button.render(screen, camera)
