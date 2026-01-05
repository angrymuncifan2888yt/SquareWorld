import pygame
from core import Camera
from assets import Sprites
from .block_breaking_stage import RendererBlockBreakingStage


class RendererGrassBlock:
    @staticmethod
    def render(screen: pygame.Surface, grass_block, camera: Camera =None):
        block_pos = camera.get_screen_position(grass_block.position) if camera else grass_block.position
        screen.blit(Sprites.GRASS_BLOCK_TEXTURE, block_pos.to_tuple())
        RendererBlockBreakingStage.render(screen, grass_block, block_pos)

