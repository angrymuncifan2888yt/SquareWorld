from .nextbot import EntityNextbot
from assets import Sound, calculate_sound_volume


class NextbotAngryMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, 1200, 2, creation_params)

    def update(self, delta: float):
        super().update(delta)
        Sound.ANGRY_MUNCI_AMBIENCE.play_looped(calculate_sound_volume(self.position, self.world.player.position, 1000))

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb