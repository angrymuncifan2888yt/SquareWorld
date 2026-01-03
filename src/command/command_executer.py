from common import ParsedCommand
from .commands import *


COMMANDS = {
    "tp": command_tp,
    "hp": command_hp,
    "spawn": command_spawn,
    "god": command_god,
    "maxhealth": command_max_health,
    "time": command_time
}
def execute_command(game_world, parsed_command: ParsedCommand):
    COMMANDS[parsed_command.name](game_world, parsed_command)
