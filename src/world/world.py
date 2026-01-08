from .entity.entity import Entity
from .entity import EntityPlayer
from typing import List
from .block.block import Block


class World:
    def __init__(self, player: EntityPlayer):
        self.entities: List[Entity] = []
        self.entities.append(player)

        self.blocks: List[Block] = []
        self.delta = 1
        self.delta_multiplier = 1.0

    @property
    def player(self) -> EntityPlayer:
        return self.entities[0]

    @player.setter
    def player(self, value): self.entities[0] = value

    def add_entity(self, entity: Entity):
        self.entities.append(entity)
    
    def add_block(self, block: Block):
        self.blocks.append(block)

    def remove_entity(self, entity):
        entity.stop_sound()
        self.entities.remove(entity)
    
    def remove_block(self, block):
        self.blocks.remove(block)

    def clear_entities(self):
        player = self.entities[0]
        copy = self.entities.copy()
        for entity in copy:
            entity.destroy()
        self.entities.append(player)
    
    def clear_blocks(self):
        self.blocks.clear()

    def update(self):
        self.delta *= self.delta_multiplier
        for entity in self.entities:
            entity.update(self.delta)

            for block in self.blocks:
                block.update(self.delta)
                if block.hitbox.collides_hitbox(entity.hitbox):
                    entity.onBlockCollision(block)

            for other in self.entities:
                if entity != other and entity.hitbox.collides_hitbox(other.hitbox):
                    entity.onEntityCollision(other)

    def stop_sound(self):
        for entity in self.entities:
            entity.stop_sound()
    