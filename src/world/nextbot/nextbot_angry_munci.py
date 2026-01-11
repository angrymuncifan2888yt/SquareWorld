from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound, Sprites
from ..components import BombImmune, HasHealth

class NextbotAngryMunci(BombImmune, EntityNextbot, HasHealth):
    @classmethod
    def image(self):
        return Sprites.ANGRY_MUNCI_TEXTURE

    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE), 1500, 2, creation_params)
        self.max_hp = 25
        self.hp = 25
    
    def on_death(self):
        self.destroy()