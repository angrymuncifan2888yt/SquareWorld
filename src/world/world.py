from .entity.entity import Entity
from .entity import *
from common import Event, EventType
from typing import List
from renderer.entity import *
from renderer.other import RendererHitbox


class World:
    def __init__(self, player: EntityPlayer):
        self.entities: List[Entity] = []
        self.entities.append(player)

    @property
    def player(self) -> EntityPlayer:
        return self.entities[0]

    @player.setter
    def player(self, value): self.entities[0] = value

    def add_entity(self, entity):
        self.entities.append(entity)

    def notify_all(self, event):
        for entity in self.entities:
            entity.handle_event(event)

    def handle_entity_events(self):
        entities_list_copy = self.entities.copy()

        for entity in entities_list_copy:
            event_list_copy: List[Event] = entity.entity_events.copy()

            for event in event_list_copy:
                self.notify_all(event)

                if event.type == EventType.TEST_EVENT:
                    print(f"DEBUG: TEst: {event.data}")

                if event.type == EventType.REMOVE_ENTITY:
                    self.entities.remove(entity)

                if event:
                    entity.entity_events.remove(event)

    def update(self, delta: float):
        self.handle_entity_events()
        self.notify_all(
            Event(EventType.PLAYER_STAT, {"hitbox": self.player.hitbox, "hp": self.player.hp, "god": self.player.god_mode})
        )

        for entity in self.entities:
            entity.update(delta)

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
