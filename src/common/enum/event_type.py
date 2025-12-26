from enum import Enum, auto


class EventType(Enum):
    TEST_EVENT = auto()
    PLAYER_STAT = auto()
    PLAYER_DAMAGE = auto()
    PLAYER_HEAL = auto()
    PLAYER_REVIVE = auto()
    PLAYER_KILL = auto()
    PLAYER_MAX_HP_SET = auto()
    PLAYER_POSITION_SET = auto()
    PLAYER_COLLISION = auto()
    PLAYER_GOD = auto()
    REMOVE_ENTITY = auto()