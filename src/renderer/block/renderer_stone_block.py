import pygame
from core import Camera
from assets import Sprites
from .block_breaking_stage import RendererBlockBreakingStage


class RendererStoneBlock:
    @staticmethod
    def render(screen: pygame.Surface, stone_block, camera: Camera =None):
        block_pos = camera.get_screen_position(stone_block.position) if camera else stone_block.position
        screen.blit(Sprites.STONE_BLOCK_TEXTURE, block_pos.to_tuple())
        RendererBlockBreakingStage.render(screen, stone_block, block_pos)

