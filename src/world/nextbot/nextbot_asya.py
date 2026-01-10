from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound, Sprites


class NextbotAsya(EntityNextbot):
    @classmethod
    def image(self):
        return Sprites.ASYA_TEXTURE
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 100, 120, AdvancedSound(SoundStorage.ASYA_AMBIENCE), 300, 2, creation_params)
