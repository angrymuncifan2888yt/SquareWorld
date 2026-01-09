from core import Hitbox
from common import const
from ..entity import Entity


class EntityBlock(Entity):
    def __init__(self, world, position, max_hardness, creation_params: dict=None):
        super().__init__(world, position, *const.BLOCK_SIZE, creation_params)
        self.max_hardness = max_hardness
        self.hardness = max_hardness

    @classmethod
    def texture(cls):
        return

    def update(self, delta: float):
        if self.hardness <= 0:
            self.world.remove_entity(self)

    def damage(self, amount=1):
        self.hardness -= amount

    def onBombExplosionCollision(self, bomb):
        if bomb.can_damage:
            self.hardness -= 3
            bomb.can_damage = False

    def onEntityCollision(self, entity):
        if not isinstance(entity, EntityBlock):
            entity.onBlockCollision(self)
