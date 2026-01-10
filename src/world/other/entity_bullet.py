from ..entity import Entity
from ..components import HasHealth
from core import Timer


class EntityBullet(Entity):
    def __init__(self, world, position, direction, creation_params = None, source=None):
        super().__init__(world, position, 25, 25, creation_params)
        self.direction = direction
        self.source = source
        self.remove_timer = Timer(10)

    def update(self, delta):
        self.remove_timer.update(delta)
        self.position.move(self.direction, 2000, delta)

        if self.remove_timer.finished:
            self.destroy()

    def onBlockCollision(self, block):
        block.damage(2)
        self.destroy()

    def onEntityCollision(self, entity):
        if isinstance(entity, HasHealth):
            if entity != self.source:
                entity.damage(9)
                self.destroy()
