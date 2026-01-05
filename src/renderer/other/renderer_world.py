from ..entity import RendererEntity
from ..block import RendererBlock
from world.entity import *
from world.block import *
from .renderer_hitbox import RendererHitbox


class RendererWorld:
    @staticmethod
    def render(screen, world, camera=None, render_hitbox=True):
        for entity in world.entities:
            RendererEntity.render(screen, entity, camera)

            if render_hitbox:
                RendererHitbox.render(screen, entity.hitbox, camera=camera)

        for block in world.blocks:
            RendererBlock.render(screen, block, camera)

            if render_hitbox:
                RendererHitbox.render(screen, block.hitbox, camera=camera)
