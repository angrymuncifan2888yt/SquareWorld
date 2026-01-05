import pygame
from core import Camera
from assets import Sprites
from .block_breaking_stage import RendererBlockBreakingStage


class RendererObsidianBlock:
    @staticmethod
    def render(screen: pygame.Surface, block, camera: Camera=None):
        block_pos = camera.get_screen_position(block.position) if camera else block.position
        screen.blit(Sprites.OBSIDIAN_BLOCK_TEXTURE, block_pos.to_tuple())

        RendererBlockBreakingStage.render(screen, block, block_pos)
