from common import ParsedCommand
from core import Position
# from world import World
from common import Event, EventType, Const
from world.entity import *


def command_tp(world: "World", parsed_command: ParsedCommand):
    pos = Position(int(parsed_command.args[0]), int(parsed_command.args[1]))
    world.notify_all(Event(EventType.PLAYER_POSITION_SET, {"position": pos}))

def command_hp(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[0] == "heal":
        if parsed_command.args[1].isdigit():
            world.notify_all(Event(EventType.PLAYER_HEAL, {"heal": int(parsed_command.args[1])}, True))
        
        elif parsed_command.args[1] == "+":
            world.notify_all(Event(EventType.PLAYER_REVIVE, {}, True))

    elif parsed_command.args[0] == "damage":
        if parsed_command.args[1].isdigit():
            world.notify_all(Event(EventType.PLAYER_DAMAGE, {"damage": int(parsed_command.args[1])}))
        
        elif parsed_command.args[1] == "kill":
            world.notify_all(Event(EventType.PLAYER_KILL, {}, True))

def command_spawn(world: "World", parsed_command: ParsedCommand):
    x = int(parsed_command.args[1])
    y = int(parsed_command.args[2])
    if parsed_command.args[0] == "triangle":
        ent = EntityTriangle(Position(x, y), parsed_command.data)
        world.add_entity(ent)

    elif parsed_command.args[0] == "medkit":
        ent = EntityMedkit(Position(x, y), parsed_command.data)
        world.add_entity(ent)

    elif parsed_command.args[0] == "platform":
        ent = EntityPlatform(Position(x, y), creation_params=parsed_command.data)
        world.add_entity(ent)

    elif parsed_command.args[0] == "bomb":
        ent = EntityBomb(Position(x, y), parsed_command.data)
        world.add_entity(ent)


def command_god(world: "World", parsed_command: ParsedCommand):
    do_god = True if parsed_command.args[0] == "True" else False

    event = Event(EventType.PLAYER_GOD, {"do_god": do_god})
    world.notify_all(event)


def command_max_health(world: "World", parsed_command: ParsedCommand):
    hp = int(parsed_command.args[0])
    world.notify_all(Event(EventType.PLAYER_MAX_HP_SET, {"max_hp": hp}))