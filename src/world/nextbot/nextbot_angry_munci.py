from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound, Sprites
from ..components import BombImmune

class NextbotAngryMunci(BombImmune, EntityNextbot):
    @classmethod
    def image(self):
        return Sprites.ANGRY_MUNCI_TEXTURE

    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE), 1500, 2, creation_params)
