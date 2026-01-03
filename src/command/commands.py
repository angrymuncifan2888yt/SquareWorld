from common import ParsedCommand
from core import Position
# from world import World
from world.entity import *


def command_tp(world: "World", parsed_command: ParsedCommand):
    pos = Position(int(parsed_command.args[0]), int(parsed_command.args[1]))
    world.player.position = pos

def command_hp(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[0] == "heal":
        if parsed_command.args[1].isdigit():
            world.player.hp.add_hp(int(parsed_command.args[1]))
        
        elif parsed_command.args[1] == "+":
            world.player.hp.revive()

    elif parsed_command.args[0] == "damage":
        if parsed_command.args[1].isdigit():
            world.player.damage(int(parsed_command.args[1]))
        
        elif parsed_command.args[1] == "kill":
            world.player.kill()

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
    world.player.god_mode = do_god


def command_max_health(world: "World", parsed_command: ParsedCommand):
    hp = int(parsed_command.args[0])
    world.player.hp.max_hp = hp


def command_time(world: "World", parsed_command: ParsedCommand):
    time = float(parsed_command.args[0])
    world.delta_multiplier = time
