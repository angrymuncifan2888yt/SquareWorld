from world.other import EntityBomb
from ..graphics import RendererText
from core import Camera
import pygame


class RendererEntityBomb:
    @staticmethod
    def render(screen: pygame.Surface, bomb: EntityBomb, camera: Camera):
        pos = camera.get_screen_position(bomb.position) if camera else bomb.position
        surface = pygame.Surface((bomb.hitbox.width, bomb.hitbox.height))
        surface.fill((0, 0, 255) if bomb.is_exploding else (255, 0, 0))
        screen.blit(surface, (pos.x, pos.y))

        if not bomb.is_exploding:
            RendererText.render(screen, bomb.text_timer, camera)