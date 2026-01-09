from common import ParsedCommand
from core import Position
# from world import World
from world.other import *
from world.nextbot import *


def command_tp(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[0] == ".":
        x = world.player.position.x
    
    else:
        x = int(parsed_command.args[0])

    if parsed_command.args[1] == ".":
        y = world.player.position.y

    else:
        y = int(parsed_command.args[1])
    world.player.position = Position(x, y)
    return f"Teleported player to {x}, {y}"

def command_hp(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[0] == "heal":
        if parsed_command.args[1].isdigit():
            world.player.hp.add_hp(int(parsed_command.args[1]))
            return "Healed player"
        
        elif parsed_command.args[1] == "+":
            world.player.hp.revive()
            return "Fully healed player"

    elif parsed_command.args[0] == "damage":
        if parsed_command.args[1].isdigit():
            world.player.damage(int(parsed_command.args[1]))
            return "Damaged player"
        
        elif parsed_command.args[1] == "kill":
            world.player.kill()
            return "Killed player"

def command_spawn(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[1] == ".":
        x = world.player.position.x
    
    else:
        x = int(parsed_command.args[1])

    if parsed_command.args[2] == ".":
        y = world.player.position.y

    else:
        y = int(parsed_command.args[2])


    if parsed_command.args[0] == "triangle":
        ent = EntityTriangle(world, Position(x, y), parsed_command.data)
        world.add_entity(ent)

    elif parsed_command.args[0] == "medkit":
        ent = EntityMedkit(world, Position(x, y), parsed_command.data)
        world.add_entity(ent)

    elif parsed_command.args[0] == "bomb":
        ent = EntityBomb(world, Position(x, y), parsed_command.data)
        world.add_entity(ent)
    
    elif parsed_command.args[0] == "angry_munci":
        ent = NextbotAngryMunci(world, Position(x, y), parsed_command.data)
        world.add_entity(ent)
    
    elif parsed_command.args[0] == "asya":
        ent = NextbotAsya(world, Position(x, y), parsed_command.data)
        world.add_entity(ent)

    elif parsed_command.args[0] == "super_munci":
        ent = NextbotSuperMunci(world, Position(x, y), parsed_command.data)
        world.add_entity(ent)

    return "Succefly spawned in entity"


def command_god(world: "World", parsed_command: ParsedCommand):
    do_god = True if parsed_command.args[0] == "True" else False
    world.player.god_mode = do_god
    if do_god:
        return "God mode: enabled"
    else:
        return "God mode: disabled"

def command_max_health(world: "World", parsed_command: ParsedCommand):
    hp = int(parsed_command.args[0])
    world.player.hp.set_max_hp(hp)
    return f"Set max health to {hp}"


def command_time(world: "World", parsed_command: ParsedCommand):
    time = float(parsed_command.args[0])
    world.delta_multiplier = time
    return f"Time: {time}"


def command_clear(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[0] == "entity":
        world.clear_entities()
        return "All entities cleared"
    
    elif parsed_command.args[0] == "block":
        world.clear_blocks()
        return "All blocks cleared"


def command_spawnpoint(world: "World", parsed_command: ParsedCommand):
    if parsed_command.args[0] == ".":
        x = world.player.position.x
    
    else:
        x = int(parsed_command.args[0])

    if parsed_command.args[1] == ".":
        y = world.player.position.y

    else:
        y = int(parsed_command.args[1])

    world.player.spawn_point = Position(x, y)
    return f"Set player spawnpoint to {x} {y}"


def command_speed(world: "World", parsed_command: ParsedCommand):
    value = parsed_command.args[0]
    if value == "default":
        value = 700

    else:
        value = int(value)

    world.player.speed = value
    return f"Set player speed to {value}"


def command_nextbotai(world: "World", parsed_command: ParsedCommand):
    value = True if parsed_command.args[0] == "True" else False
    world.nextbot_ai = value
    if value == True:
        return "Nextbot AI: on"

    else:
        return "Nextbot AI: disabled"
