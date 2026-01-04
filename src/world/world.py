from .entity.entity import Entity
from .entity import *
from typing import List
from renderer.entity import *
from .block import *
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

    def clear_entities(self):
        player = self.entities[0]
        self.entities.clear()
        self.entities.append(player)
    
    def clear_blocks(self):
        self.blocks.clear()

    def update(self):
        self.delta *= self.delta_multiplier
        for entity in self.entities:
            if not entity.alive:
                self.entities.remove(entity)
                
            entity.update(self.delta)

            for block in self.blocks:
                if block.hitbox.collides_hitbox(entity.hitbox):
                    entity.onBlockCollision(block)

            for other in self.entities:
                if entity != other and entity.hitbox.collides_hitbox(other.hitbox):
                    entity.onEntityCollision(other)
