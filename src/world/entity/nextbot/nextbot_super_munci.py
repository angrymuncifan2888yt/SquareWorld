from .nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound, calculate_sound_volume

class NextbotSuperMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, AdvancedSound(SoundStorage.SUPER_MUNCI_AMBIENCE), 5000, 1.5, creation_params)

    def update(self, delta: float):
        super().update(delta)

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb
