from .nextbot import EntityNextbot


class NextbotAngryMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 150, 150, 1000, 2, creation_params)
