from .block import Block
from assets import Sprites


class ObsidianBlock(Block):
    def __init__(self, world, position):
        super().__init__(world, position, 10)

    @classmethod
    def texture(cls):
        return Sprites.OBSIDIAN_BLOCK_TEXTURE