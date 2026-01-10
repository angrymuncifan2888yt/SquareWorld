from world.other import EntityBullet
from core import Camera
import pygame


class RendererEntityBullet:
    @staticmethod
    def render(screen: pygame.Surface, bullet: EntityBullet, camera: Camera):
        pos = camera.get_screen_position(bullet.position) if camera else bullet.position
        surface = pygame.Surface((bullet.hitbox.width, bullet.hitbox.height))
        surface.fill((0, 255, 255))
        screen.blit(surface, (pos.x, pos.y))
