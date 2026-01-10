from dataclasses import dataclass
import const


@dataclass
class ParsedCommand:
    name: str
    args: list
    data: dict