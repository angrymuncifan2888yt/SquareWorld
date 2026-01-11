from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound, Sprites
from ..components import HasHealth


class NextbotAsya(EntityNextbot, HasHealth):
    @classmethod
    def image(self):
        return Sprites.ASYA_TEXTURE
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 100, 120, AdvancedSound(SoundStorage.ASYA_AMBIENCE), 700, 2, creation_params)
        self.max_hp = 10
        self.hp = 10
    
    def on_death(self):
        self.destroy()