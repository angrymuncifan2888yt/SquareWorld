from .nextbot import EntityNextbot
from assets import Sound, calculate_sound_volume

class NextbotSuperMunci(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, 5000, 1.5, creation_params)

    def update(self, delta: float):
        super().update(delta)
        Sound.SUPER_MUNCI_AMBIENCE.play_looped(calculate_sound_volume(self.position, self.world.player.position, 1500))

    def onBombExplosionCollision(self, bomb):
        pass  # Immune to bomb

    def destroy(self):
        Sound.SUPER_MUNCI_AMBIENCE.stop()
        super().destroy()
    
    def stop(self):
        Sound.SUPER_MUNCI_AMBIENCE.stop()