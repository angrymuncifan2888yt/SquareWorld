from .entity_nextbot import EntityNextbot
from assets import SoundStorage, AdvancedSound
from ..components import BombImmune
from .nextbot_angry_munci import NextbotAngryMunci
from .nextbot_king_munci import NextbotKingMunci

class NextbotSuperMunci(BombImmune, EntityNextbot):
    def __init__(self, world, position, creation_params=None):
        super().__init__(world, position, 120, 120, AdvancedSound(SoundStorage.SUPER_MUNCI_AMBIENCE), 9000, 1.5, creation_params)

    def onEntityCollision(self, entity):
        super().onEntityCollision(entity)
        # Spawning in King Munci if in collision with angry_munci
        if isinstance(entity, NextbotAngryMunci):
            king = NextbotKingMunci(self.world, self.position.copy())
            self.world.add_entity(king)

            # Removing Angry Munci and Super Munci
            entity.destroy()
            self.destroy()