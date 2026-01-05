from .entity import Entity
from .entity_player import EntityPlayer


class EntityMedkit(Entity):
    def __init__(self, world, position, creation_params: dict = None):
        super().__init__(world, position, 25, 25, creation_params)

    def onEntityCollision(self, entity):
        if isinstance(entity, EntityPlayer):
            if entity.hp.hp < entity.hp.max_hp:
                entity.add_hp(40)
                self.world.remove_entity(self)
