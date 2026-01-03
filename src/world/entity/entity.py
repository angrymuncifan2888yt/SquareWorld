from core import Hitbox
from abc import ABC
from common.interface import ILogical

class Entity(ILogical, ABC):
    def __init__(self, position, width, height, creation_params: dict = None):
        super().__init__()
        self.alive = True
        self.hitbox = Hitbox(position, width, height)

        if isinstance(creation_params, dict):
            if creation_params.get("width"):
                self.hitbox.width = int(creation_params["width"])
            if creation_params.get("height"):
                self.hitbox.height = int(creation_params["height"])

    def update(self, delta: float):
        pass

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value

    def onCollision(self, entity):
        pass
