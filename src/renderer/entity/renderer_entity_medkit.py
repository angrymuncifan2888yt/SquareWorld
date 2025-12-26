from common.interface import IRenderer
from world.entity import EntityMedkit
from core import Camera
import pygame


class RendererEntityMedkit(IRenderer):
    @staticmethod
    def render(screen: pygame.Surface, medkit: EntityMedkit, camera: Camera):
        pos = camera.get_screen_position(medkit.position) if camera else medkit.position
        surface = pygame.Surface((medkit.hitbox.width, medkit.hitbox.height))
        surface.fill((255, 255, 0))
        screen.blit(surface, (pos.x, pos.y))
