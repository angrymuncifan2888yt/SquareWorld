from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound, Sprites
from ..components import HasHealth
from core import Timer

class NextbotKingMunci(EntityNextbot, HasHealth):
    @classmethod
    def image(self):
        return Sprites.KING_MUNCI_TEXTURE
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 220, 260, AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE), 900, 2, creation_params)
        self.max_hp = 1000
        self.hp = self.max_hp
        self.block_break_timer = Timer(0.2)
        self.can_damage_block = False
        SoundStorage.KING_MUNCI_ROAR.play()

    def update(self, delta):
        super().update(delta)
        if not self.can_damage_block:
            self.block_break_timer.update(delta)

        if self.block_break_timer.finished:
            self.can_damage_block = True
    
    def onBlockCollision(self, block):
        super().onBlockCollision(block)
        if self.can_damage_block:
            block.damage(4)
            self.can_damage_block = False
            self.block_break_timer.reset()

    def on_death(self):
        self.destroy()
    
    def onBombExplosionCollision(self, bomb):
        if bomb.can_damage:
            self.damage(200)
            bomb.can_damage = False
        