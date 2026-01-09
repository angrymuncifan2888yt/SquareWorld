from .entity_block import EntityBlock
from assets import Sprites


class StoneBlock(EntityBlock):
    def __init__(self, world, position):
        super().__init__(world, position, 3)

    @classmethod
    def texture(cls):
        return Sprites.STONE_BLOCK_TEXTURE