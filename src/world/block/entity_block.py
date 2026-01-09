from core import Hitbox
from common import const
from ..entity import Entity


class EntityBlock(Entity):
    def __init__(self, world, position, max_hardness, creation_params: dict=None):
        # Initialize a block entity with standard block size
        super().__init__(world, position, *const.BLOCK_SIZE, creation_params)
        self.max_hardness = max_hardness  # Maximum hardness of the block
        self.hardness = max_hardness      # Current hardness (health) of the block

    @classmethod
    def texture(cls):
        # Placeholder method to return the block's texture
        return

    def update(self, delta: float):
        # Remove the block from the world if hardness reaches zero
        if self.hardness <= 0:
            self.world.remove_entity(self)

    def damage(self, amount=1):
        # Reduce the block's hardness by a specified amount
        self.hardness -= amount

    def onBombExplosionCollision(self, bomb):
        # Handle damage from a bomb explosion
        if bomb.can_damage:
            self.hardness -= 3  # Blocks take 3 damage from bomb
            bomb.can_damage = False  # Prevent repeated damage in the same explosion

    def onEntityCollision(self, entity):
        # Forward collision handling to the colliding entity unless it's another block
        if not isinstance(entity, EntityBlock):
            entity.onBlockCollision(self)
