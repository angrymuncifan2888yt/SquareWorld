from graphics import Text
from core import Camera
import pygame


class RendererText:
    @staticmethod
    def render(
        surface: pygame.Surface,
        text: Text,
        camera: Camera | None = None
    ):
        text_surface = text.font.render(
            text.text,
            True,
            text.color
        )

        if camera:
            pos = camera.get_screen_position(text.position)
            surface.blit(text_surface, (pos.x, pos.y))
        else:
            surface.blit(
                text_surface,
                (text.position.x, text.position.y)
            )