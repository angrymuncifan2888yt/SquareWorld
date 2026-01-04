from world.entity import EntityTriangle
from core import Camera
import pygame


class RendererEntityTriangle:
    @staticmethod
    def render(screen: pygame.Surface, triangle: EntityTriangle, camera: Camera = None):
        pos = triangle.hitbox.position
        w = triangle.hitbox.width
        h = triangle.hitbox.height

        if camera:
            pos = camera.get_screen_position(pos)

        points = [
            (pos.x + w // 2, pos.y), 
            (pos.x, pos.y + h),              
            (pos.x + w, pos.y + h)     
        ]

        pygame.draw.polygon(screen, (255, 0, 0), points)
