from core import Hitbox, Camera
import pygame


class RendererHitbox:
    @staticmethod
    def render(surface: pygame.Surface, hitbox: Hitbox,
               color: tuple[int, int, int]=(255, 255, 255),
               camera: Camera | None = None):
        if camera:
            pos = camera.get_screen_position(hitbox.position)
        else:
            pos = (hitbox.position.x, hitbox.position.y)

        rect = pygame.Rect(
            *pos,
            hitbox.width,
            hitbox.height
        )

        pygame.draw.rect(surface, color, rect, 2)