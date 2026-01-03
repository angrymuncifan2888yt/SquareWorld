from .entity.entity import Entity
from .entity import *
from typing import List
from renderer.entity import *
from renderer.other import RendererHitbox


class World:
    def __init__(self, player: EntityPlayer):
        self.entities: List[Entity] = []
        self.entities.append(player)
        self.delta = 1
        self.delta_multiplier = 1.0

    @property
    def player(self) -> EntityPlayer:
        return self.entities[0]

    @player.setter
    def player(self, value): self.entities[0] = value

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        self.delta *= self.delta_multiplier
        for entity in self.entities:
            if not entity.alive:
                self.entities.remove(entity)
                
            entity.update(self.delta)

            for other in self.entities:
                if entity != other and entity.hitbox.collides_hitbox(other.hitbox):
                    entity.onCollision(other)

    def render(self, screen, camera=None, render_hitbox=True):
        for entity in self.entities:
            if isinstance(entity, EntityPlayer):
                RendererEntityPlayer.render(screen, entity, camera)

            elif isinstance(entity, EntityTriangle):
                RendererEntityTriangle.render(screen, entity, camera)
            
            elif isinstance(entity, EntityPlatform):
                RendererEntityPlatform.render(screen, entity, camera)

            elif isinstance(entity, EntityMedkit):
                RendererEntityMedkit.render(screen, entity, camera)

            elif isinstance(entity, EntityBomb):
                RendererEntityBomb.render(screen, entity, camera)

            if render_hitbox:
                RendererHitbox.render(screen, entity.hitbox, camera=camera)
