import pygame
from core import Camera


class RendererGrassBlock:
    @staticmethod
    def render(screen: pygame.Surface, grass_block, camera: Camera =None):
        block_pos = camera.get_screen_position(grass_block.position) if camera else grass_block.position
        surf = pygame.Surface((100, 100))
        surf.fill((150, 75, 0))
        screen.blit(surf, block_pos.to_tuple())
