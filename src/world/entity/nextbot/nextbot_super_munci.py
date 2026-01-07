from .nextbot import EntityNextbot


class NextbotSuperMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, 5000, 1.5, creation_params)

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb