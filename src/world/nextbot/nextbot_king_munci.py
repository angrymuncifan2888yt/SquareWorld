from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound
from ..components import BombImmune

class NextbotKingMunci(BombImmune, EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 140, AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE), 20000, 2, creation_params)
