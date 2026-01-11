from graphics import HpBar
from core import Camera, Position
from .renderer_text import RendererText
from graphics.text import Text
from assets import Fonts
import pygame


class RendererHpBar:
    @staticmethod
    def render(
        screen: pygame.Surface,
        hp_bar: HpBar,
        camera: Camera = None,
        text: str | None = None
    ):
        hp_bar_pos = camera.get_screen_position(hp_bar.position) if camera else hp_bar.position

        # Background
        pygame.draw.rect(
            screen,
            hp_bar.background_color,
            (hp_bar_pos.x, hp_bar_pos.y, hp_bar.hitbox.width, hp_bar.hitbox.height)
        )

        # Fill
        fill_width = int(hp_bar.hitbox.width * (hp_bar.value / hp_bar.max_value))
        pygame.draw.rect(
            screen,
            hp_bar.fill_color,
            (hp_bar_pos.x, hp_bar_pos.y, fill_width, hp_bar.hitbox.height)
        )

        # Border
        pygame.draw.rect(
            screen,
            hp_bar.border_color,
            (hp_bar_pos.x, hp_bar_pos.y, hp_bar.hitbox.width, hp_bar.hitbox.height),
            5
        )

        # Optional text (name / hp)
        if text:
            text_obj = Text(
                text,
                Position(0, 0),
                Fonts.FONT_30
            )
            text_obj.center_in_hitbox(hp_bar.hitbox)
            RendererText.render(screen, text_obj)
