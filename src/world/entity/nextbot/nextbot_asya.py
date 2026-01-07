from .nextbot import EntityNextbot


class NextbotAsya(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 100, 120, 300, 2, creation_params)
