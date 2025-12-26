from .entity import Entity
from common import HpSystem, Event, EventType
from common import Const
from assets import Sound


class EntityPlayer(Entity):
    def __init__(self, position, creation_params: dict = None):
        super().__init__(position, 100, 100, creation_params)
        self.hp = HpSystem(Const.PLAYER_MAX_HP)
        self.god_mode = False

    def handle_event(self, event: Event):
        if self.hp.is_dead:
            self.position.x = 0
            self.position.y = 0
            self.hp.revive()

        if event.type == EventType.PLAYER_HEAL:
            self.hp.add_hp(event.data["heal"])
            Sound.heal()

        elif event.type == EventType.PLAYER_GOD:
            self.god_mode = event.data["do_god"]

        elif event.type == EventType.PLAYER_MAX_HP_SET:
            self.hp.set_max_hp(event.data["max_hp"])

        elif event.type == EventType.PLAYER_REVIVE:
            self.hp.revive()

        elif event.type == EventType.PLAYER_POSITION_SET:
            self.position = event.data["position"]

        if not self.god_mode:
            if event.type == EventType.PLAYER_DAMAGE:
                self.hp.damage(event.data["damage"])
                Sound.damage()

            elif event.type == EventType.PLAYER_KILL:
                self.hp.kill()
                Sound.damage()

            elif event.type == EventType.PLAYER_COLLISION:
                self.hitbox.handle_collision(event.data["hitbox"])