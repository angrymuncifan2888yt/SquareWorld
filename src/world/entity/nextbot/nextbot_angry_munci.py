from .nextbot import EntityNextbot


class NextbotAngryMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, 1200, 2, creation_params)
