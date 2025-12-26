from .entity import Entity
from core import Timer
from common import Event, EventType


class EntityTriangle(Entity):
    def __init__(self, position, creation_params: dict = None):
        super().__init__(position, 100, 100, creation_params)
        self.damage_timer = Timer(2)

    def handle_event(self, event: Event):
        if event.type == EventType.PLAYER_STAT:
            if self.damage_timer.finished:
                if event.data["hitbox"].collides_hitbox(self.hitbox):
                    event_to_emit = Event(EventType.PLAYER_DAMAGE, {"damage": 40}, True)
                    self.emit_event(event_to_emit)
                    self.damage_timer.reset()

    def update(self, delta: float):
        self.damage_timer.update(delta)
