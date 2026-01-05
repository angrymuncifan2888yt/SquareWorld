import pygame
from core import Camera
from common import const
from assets import Sprites


class RendererGrassBlock:
    @staticmethod
    def render(screen: pygame.Surface, grass_block, camera: Camera =None):
        block_pos = camera.get_screen_position(grass_block.position) if camera else grass_block.position
        screen.blit(Sprites.GRASS_BLOCK_TEXTURE, block_pos.to_tuple())
