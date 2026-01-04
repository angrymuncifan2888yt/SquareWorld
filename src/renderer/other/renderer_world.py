from ..entity import *
from ..block import *
from world.entity import *
from world.block import *
from .renderer_hitbox import RendererHitbox


class RendererWorld:
    @staticmethod
    def render(screen, world, camera=None, render_hitbox=True):
        for entity in world.entities:
            if isinstance(entity, EntityPlayer):
                RendererEntityPlayer.render(screen, entity, camera)

            elif isinstance(entity, EntityTriangle):
                RendererEntityTriangle.render(screen, entity, camera)

            elif isinstance(entity, EntityMedkit):
                RendererEntityMedkit.render(screen, entity, camera)

            elif isinstance(entity, EntityBomb):
                RendererEntityBomb.render(screen, entity, camera)

            if render_hitbox:
                RendererHitbox.render(screen, entity.hitbox, camera=camera)

        for block in world.blocks:
            if isinstance(block, GrassBlock):
                RendererGrassBlock.render(screen, block, camera)
            
            elif isinstance(block, ObsidianBlock):
                RendererObsidianBlock.render(screen, block, camera)
                
            if render_hitbox:
                RendererHitbox.render(screen, block.hitbox, camera=camera)
