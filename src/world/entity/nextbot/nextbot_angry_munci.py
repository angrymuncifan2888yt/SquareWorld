from .nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound


class NextbotAngryMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE), 1500, 2, creation_params)

    def update(self, delta: float):
        super().update(delta)

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb
