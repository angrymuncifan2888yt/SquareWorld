from .entity import Entity
from common import EventType, Event, Const


class EntityMedkit(Entity):
    def __init__(self, position, creation_params: dict = None):
        super().__init__(position, 25, 25, creation_params)

    def handle_event(self, event):
        if event.type == EventType.PLAYER_STAT:
            if event.data["hp"].hp < event.data["hp"].max_hp:
                if event.data["hitbox"].collides_hitbox(self.hitbox):
                    self.emit_event(Event(EventType.PLAYER_HEAL, {"heal": 40}))
                    self.emit_event(Event(EventType.REMOVE_ENTITY, {}))
