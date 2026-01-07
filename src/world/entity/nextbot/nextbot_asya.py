from .nextbot import EntityNextbot
from assets import Sound, calculate_sound_volume


class NextbotAsya(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 100, 120, 300, 2, creation_params)

    def update(self, delta: float):
        super().update(delta)
        Sound.ASYA_AMBIENCE.play_looped(calculate_sound_volume(self.position, self.world.player.position, 1000))
