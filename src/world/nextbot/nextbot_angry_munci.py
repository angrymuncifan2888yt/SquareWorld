from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound
from ..components import BombImmune

class NextbotAngryMunci(BombImmune, EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE), 1500, 2, creation_params)
