from ..entity import Entity
from .entity_player import EntityPlayer


class EntityMedkit(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        # Initialize a small medkit entity with size 25x25
        super().__init__(world, position, 25, 25, creation_params)

    def onEntityCollision(self, entity):
        # When a player collides with the medkit
        if isinstance(entity, EntityPlayer):
            # Only heal if player's HP is not full
            if entity.hp < entity.max_hp:
                entity.heal(40)  # Heal the player by 40 HP
                self.destroy()
