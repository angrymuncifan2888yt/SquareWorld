from .entity import Entity
from common import Event, EventType


class EntityPlatform(Entity):
    def __init__(self, position, width=200, height=50, creation_params: dict = None):
        super().__init__(position, width, height, creation_params)

    def update(self, delta: float):
        pass

    def handle_event(self, event: Event):
        if event.type == EventType.PLAYER_STAT:
            if event.data["hitbox"].collides_hitbox(self.hitbox):
                self.emit_event(Event(EventType.PLAYER_COLLISION, {"hitbox": self.hitbox}))
