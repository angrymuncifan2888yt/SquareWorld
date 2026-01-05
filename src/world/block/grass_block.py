from .block import Block
from assets import Sprites


class GrassBlock(Block):
    def __init__(self, world, position):
        super().__init__(world, position, 1)

    @classmethod
    def texture(cls):
        return Sprites.GRASS_BLOCK_TEXTURE