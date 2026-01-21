from .parsed_command import ParsedCommand
import json

def parse_command(text: str) -> ParsedCommand | None:
    text = text.strip()
    if not text:
        return None

    json_data = {}
    if "{" in text:
        text, json_part = text.split("{", 1)
        json_data = json.loads("{" + json_part)

    parts = text.split()
    name = parts[0]
    args = parts[1:]

    return ParsedCommand(name, args, json_data)
