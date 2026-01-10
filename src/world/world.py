from .entity import Entity
from .block.entity_block import EntityBlock
from .nextbot.entity_nextbot import EntityNextbot
from .other import EntityPlayer
from typing import List


class World:
    def __init__(self, player: EntityPlayer):
        self.entities: List[Entity] = []
        self.entities.append(player)

        # Time
        self.delta = 1
        self.delta_multiplier = 1.0

        # Nextbots settings
        self.nextbot_ai = True
        self.nextbot_sound = True

    # Player property/setter so entities can write world.player...
    @property
    def player(self) -> EntityPlayer:
        return self.entities[0]

    @player.setter
    def player(self, value): self.entities[0] = value

    # Adds an entity
    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    # Removes an entity
    def remove_entity(self, entity):
        entity.stop_sound()
        self.entities.remove(entity)

    # Clears all entities
    def clear_entities(self):
        for e in self.entities[1:]:
            e.destroy()

    # Clear all blocks
    def clear_blocks(self):
        new_entities = [e for e in self.entities if not isinstance(e, EntityBlock)]

        for e in self.entities:
            if isinstance(e, EntityBlock):
                e.destroy()
        self.entities = new_entities

    # Clears all nextbots
    def clear_nextbots(self):
        for e in self.entities[:]:
            if isinstance(e, EntityNextbot):
                e.destroy()

    # Disable all nextbots sound
    def disable_nextbots_sound(self):
        self.nextbot_sound = False
        for nextbot in self.entities:
            if isinstance(nextbot, EntityNextbot):
                nextbot.stop_sound()

    # Update all entities and world itself
    def update(self):
        self.delta *= self.delta_multiplier
        for entity in self.entities:
            entity.update(self.delta)

            # Checking collision with all other entities
            for other in self.entities:
                if entity != other and entity.hitbox.collides_hitbox(other.hitbox):
                    entity.onEntityCollision(other)

    def stop_sound(self):
        for entity in self.entities:
            entity.stop_sound()
    