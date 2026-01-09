from .entity_block import EntityBlock
from assets import Sprites


class ObsidianBlock(EntityBlock):
    def __init__(self, world, position):
        super().__init__(world, position, 10)

    @classmethod
    def texture(cls):
        return Sprites.OBSIDIAN_BLOCK_TEXTURE