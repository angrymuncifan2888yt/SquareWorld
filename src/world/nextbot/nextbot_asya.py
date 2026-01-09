from .nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound


class NextbotAsya(EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 100, 120, AdvancedSound(SoundStorage.ASYA_AMBIENCE), 300, 2, creation_params)
