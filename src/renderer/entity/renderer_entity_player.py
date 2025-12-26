from common.interface import IRenderer
from world.entity import EntityPlayer
from core import Camera
import pygame


class RendererEntityPlayer(IRenderer):
    @staticmethod
    def render(screen: pygame.Surface, player: EntityPlayer, camera: Camera = None):
        player_pos = camera.get_screen_position(player.position) if camera else player.position

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            pygame.Rect(player_pos.x, player_pos.y,
                        player.hitbox.width, player.hitbox.height)
        )
