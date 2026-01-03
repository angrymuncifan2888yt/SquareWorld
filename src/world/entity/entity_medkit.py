from .entity import Entity


class EntityMedkit(Entity):
    def __init__(self, position, creation_params: dict = None):
        super().__init__(position, 25, 25, creation_params)
