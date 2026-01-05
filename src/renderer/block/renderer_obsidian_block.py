import pygame
from core import Camera
from assets import Sprites
from common import const


class RendererObsidianBlock:
    @staticmethod
    def render(screen: pygame.Surface, block, camera: Camera=None):
        block_pos = camera.get_screen_position(block.position) if camera else block.position

        surf = pygame.Surface(const.BLOCK_SIZE)
        surf.fill((30, 30, 30))
        screen.blit(surf, block_pos.to_tuple())

        if block.hardness < block.max_hardness and Sprites.BREAKING_STAGES:
            progress = (block.max_hardness - block.hardness) / block.max_hardness
            stage_index = int(progress * len(Sprites.BREAKING_STAGES))
            stage_index = min(stage_index, len(Sprites.BREAKING_STAGES) - 1)

            crack_surf = Sprites.BREAKING_STAGES[stage_index]
            screen.blit(crack_surf, block_pos.to_tuple())
