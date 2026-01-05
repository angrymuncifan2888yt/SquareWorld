import pygame
from core import Camera
from .renderer_grass_block import RendererGrassBlock
from .renderer_obsidian_block import RendererObsidianBlock
from world.block import *


class RendererBlock:
    render_list = {
        GrassBlock: RendererGrassBlock,
        ObsidianBlock: RendererObsidianBlock
    }
    @staticmethod
    def render(screen: pygame.Surface, block, camera: Camera=None):
        RendererBlock.render_list[type(block)].render(screen, block, camera)
