from core import Hitbox
from abc import ABC, abstractmethod
from common.interface import IEventful, ILogical

class Entity(IEventful, ILogical, ABC):
    def __init__(self, position, width, height, creation_params: dict = None):
        super().__init__()
        self.hitbox = Hitbox(position, width, height)


        if isinstance(creation_params, dict):
            if creation_params.get("width"):
                self.hitbox.width = int(creation_params["width"])
            if creation_params.get("height"):
                self.hitbox.height = int(creation_params["height"])

    def update(self, delta: float):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value
