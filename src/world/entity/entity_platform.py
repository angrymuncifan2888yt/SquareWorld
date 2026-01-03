from .entity import Entity


class EntityPlatform(Entity):
    def __init__(self, position, width=200, height=50, creation_params: dict = None):
        super().__init__(position, width, height, creation_params)
