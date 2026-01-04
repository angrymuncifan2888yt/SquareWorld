from .entity import Entity
from .entity_medkit import EntityMedkit
from .entity_triangle import EntityTriangle
from .entity_bomb import EntityBomb
from common import HpSystem
from common import Const
from assets import Sound


class EntityPlayer(Entity):
    def __init__(self, position, creation_params: dict = None):
        super().__init__(position, 100, 100, creation_params)
        self.hp = HpSystem(Const.PLAYER_MAX_HP)
        self.god_mode = False

    def update(self, delta):
        if self.hp.is_dead:
            self.position.x = 0
            self.position.y = 0
            self.hp.revive()

    def damage(self, hp):
        self.hp.damage(hp)
        Sound.damage()
    
    def kill(self):
        self.hp.kill()
        Sound.damage()
        
    def onEntityCollision(self, entity):
        if isinstance(entity, EntityMedkit):
            if not self.hp.hp >= self.hp.max_hp:
                self.hp.add_hp(40)
                entity.alive = False
                Sound.heal()

        if not self.god_mode:
            if isinstance(entity, EntityTriangle):
                if entity.can_damage:
                    self.damage(40)
                    entity.can_damage = False
                    Sound.damage()

            elif isinstance(entity, EntityBomb):
                if entity.is_exploding:
                    self.damage(200)
                    Sound.damage()

    def onBlockCollision(self, block):
        if not self.god_mode:
            self.hitbox.handle_collision(block.hitbox)
