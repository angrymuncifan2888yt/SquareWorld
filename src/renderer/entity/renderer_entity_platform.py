from common.interface import IRenderer
from world.entity import EntityPlatform
from core import Camera
import pygame


class RendererEntityPlatform(IRenderer):
    @staticmethod
    def render(screen: pygame.Surface, platform: EntityPlatform, camera: Camera = None):
        platform_pos = camera.get_screen_position(platform.position) if camera else platform.position

        pygame.draw.rect(
            screen,
            (0, 0, 255),
            pygame.Rect(platform_pos.x, platform_pos.y,
                        platform.hitbox.width, platform.hitbox.height)
        )
