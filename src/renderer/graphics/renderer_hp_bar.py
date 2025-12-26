from common.interface import IRenderer
from graphics import HpBar
from core import Camera
from .renderer_text import RendererText
import pygame


class RendererHpBar(IRenderer):
    @staticmethod
    def render(screen: pygame.Surface, hp_bar: HpBar, camera: Camera = None):
        hp_bar_pos = camera.get_screen_position(hp_bar.position) if camera else hp_bar.position

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (hp_bar_pos.x, hp_bar_pos.y, hp_bar.hitbox.width, hp_bar.hitbox.height)
        )

        fill_width = int(hp_bar.hitbox.width * (hp_bar.value / hp_bar.max_value))
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (hp_bar_pos.x, hp_bar_pos.y, fill_width, hp_bar.hitbox.height)
        )

        border_thickness = 5
        pygame.draw.rect(
            screen,
            (100, 100, 100),
            (hp_bar_pos.x, hp_bar_pos.y, hp_bar.hitbox.width, hp_bar.hitbox.height),
            border_thickness
        )

        # Text
        RendererText.render(screen, hp_bar.text, camera)
