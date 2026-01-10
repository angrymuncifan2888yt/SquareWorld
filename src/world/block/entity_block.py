import const
from ..entity import Entity
from ..components import HasHealth


class EntityBlock(Entity, HasHealth):
    def __init__(self, world, position, max_hardness, creation_params: dict=None):
        # Initialize a block entity with standard block size
        super().__init__(world, position, *const.BLOCK_SIZE, creation_params)
        self.max_hp = max_hardness
        self.hp = max_hardness

    @classmethod
    def texture(cls):
        # Placeholder method to return the block's texture
        return

    def on_death(self):
        self.destroy()

    def onBombExplosionCollision(self, bomb):
        # Handle damage from a bomb explosion
        if bomb.can_damage:
            self.damage(3)
            bomb.can_damage = False  # Prevent repeated damage in the same explosion

    def onEntityCollision(self, entity):
        # Forward collision handling to the colliding entity unless it's another block
        if not isinstance(entity, EntityBlock):
            entity.onBlockCollision(self)
