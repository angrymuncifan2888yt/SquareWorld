from world.other import EntityBomb
from core import Camera, Position
from graphics import Text
from assets import Fonts
import pygame


class RendererEntityBomb:
    @staticmethod
    def render(screen: pygame.Surface, bomb: EntityBomb, camera: Camera):
        pos = camera.get_screen_position(bomb.position) if camera else bomb.position
        surface = pygame.Surface((bomb.hitbox.width, bomb.hitbox.height))
        surface.fill((0, 0, 255) if bomb.is_exploding else (255, 0, 0))
        screen.blit(surface, (pos.x, pos.y))

        if not bomb.is_exploding:
            # Text object to show countdown timer on the bomb
            text_timer = Text(str(round(bomb.defuse_timer.time_left, 1)), Position(0, 0), Fonts.FONT_30)
            text_timer.center_in_hitbox(bomb.hitbox)
            text_timer.render(screen, camera)