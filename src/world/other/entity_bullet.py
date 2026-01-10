from ..entity import Entity
from ..components import HasHealth


class EntityBullet(Entity):
    def __init__(self, world, position, direction, creation_params = None):
        super().__init__(world, position, 25, 25, creation_params)
        self.direction = direction

    def update(self, delta):
        self.position.move(self.direction, 2000, delta)

    def onBlockCollision(self, block):
        block.damage(2)
        self.destroy()

    def onEntityCollision(self, entity):
        if isinstance(entity, HasHealth):
            entity.damage(9)
            self.destroy()
