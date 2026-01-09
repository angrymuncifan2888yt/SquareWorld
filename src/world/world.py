from .entity import Entity
from .block.entity_block import EntityBlock
from .nextbot.nextbot import EntityNextbot
from .other import EntityPlayer
from typing import List


class World:
    def __init__(self, player: EntityPlayer):
        self.entities: List[Entity] = []
        self.entities.append(player)

        self.delta = 1
        self.delta_multiplier = 1.0
        self.nextbot_ai = True

    @property
    def player(self) -> EntityPlayer:
        return self.entities[0]

    @player.setter
    def player(self, value): self.entities[0] = value

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        entity.stop_sound()
        self.entities.remove(entity)

    def clear_entities(self):
        for e in self.entities[1:]:
            e.destroy()

    def clear_blocks(self):
        new_entities = [e for e in self.entities if not isinstance(e, EntityBlock)]

        for e in self.entities:
            if isinstance(e, EntityBlock):
                e.destroy()
        self.entities = new_entities

    def clear_nextbots(self):
        for e in self.entities[:]:
            if isinstance(e, EntityNextbot):
                e.destroy()

    def update(self):
        self.delta *= self.delta_multiplier
        for entity in self.entities:
            entity.update(self.delta)

            for other in self.entities:
                if entity != other and entity.hitbox.collides_hitbox(other.hitbox):
                    entity.onEntityCollision(other)

    def stop_sound(self):
        for entity in self.entities:
            entity.stop_sound()
    