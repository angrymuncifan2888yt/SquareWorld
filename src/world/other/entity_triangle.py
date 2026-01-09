from ..entity import Entity
from .entity_player import EntityPlayer
from core import Timer


class EntityTriangle(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        # Initialize the triangle entity with a default size of 100x100
        super().__init__(world, position, 100, 100, creation_params)

        # Set up the damage timer, either from creation_params or default to 2 seconds
        if creation_params:
            if creation_params.get("damage_timer"):
                self.damage_timer = Timer(creation_params.get("damage_timer"))
            else:
                self.damage_timer = Timer(2)
        else:
            self.damage_timer = Timer(2)

        self.can_damage = False  # Flag indicating whether the triangle can currently deal damage

    def update(self, delta: float):
        # Update the damage timer if the triangle cannot currently deal damage
        if not self.can_damage:
            self.damage_timer.update(delta)

        # Once the timer finishes, allow the triangle to damage again and reset the timer
        if self.damage_timer.finished:
            self.can_damage = True
            self.damage_timer.reset()

    def onEntityCollision(self, entity):
        # Handle collision with another entity
        if isinstance(entity, EntityPlayer):
            # If the triangle can deal damage, inflict damage to the player
            if self.can_damage:
                entity.damage(40)
                self.can_damage = False  # Disable further damage until timer resets
