from .entity import Entity
from .entity_player import EntityPlayer
from core import Timer


class EntityTriangle(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        super().__init__(world, position, 100, 100, creation_params)
        if creation_params:
            if creation_params.get("damage_timer"):
                self.damage_timer = Timer(creation_params.get("damage_timer"))
            
            else:
                self.damage_timer = Timer(2)

        else:
            self.damage_timer = Timer(2)
            
        self.can_damage = False

    def update(self, delta: float):
        if not self.can_damage:
            self.damage_timer.update(delta)

        if self.damage_timer.finished:
            self.can_damage = True
            self.damage_timer.reset()

    def onEntityCollision(self, entity):
        if isinstance(entity, EntityPlayer):
            if self.can_damage:
                entity.damage(40)
                self.can_damage = False