from ..entity import Entity
from ..components import HasHealth


class EntityMedkit(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        # Initialize a small medkit entity with size 25x25
        super().__init__(world, position, 25, 25, creation_params)

    def onEntityCollision(self, entity):
        # When a entity with health system collides with the medkit
        if isinstance(entity, HasHealth):
            # Only heal if entity HP is not full
            if entity.hp < entity.max_hp:
                entity.heal(40)  # Heal the entity by 40 HP
                self.destroy()
