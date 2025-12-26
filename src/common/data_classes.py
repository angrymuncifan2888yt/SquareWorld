from idlelib.configdialog import help_pages

from .enum.event_type import EventType
from dataclasses import dataclass
from .const import Const


@dataclass
class Event:
    type: EventType
    data: dict
    delete_after_process: bool = True


@dataclass
class HpSystem:
    hp: int
    is_dead: bool = False
    max_hp: int = Const.PLAYER_MAX_HP

    def damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.is_dead = True
            self.hp = 0

    def kill(self):
        self.damage(self.max_hp)
        self.is_dead = True

    def set_max_hp(self, hp: int):
        self.max_hp = hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def add_hp(self, hp):
        self.hp += hp
        if self.hp > self.max_hp:
            self.hp = Const.PLAYER_MAX_HP

    def revive(self):
        self.hp = self.max_hp
        self.is_dead = False


@dataclass
class ParsedCommand:
    name: str
    args: list
    data: dict