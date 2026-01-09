from ..entity import RendererEntity
from world.other import *
from world.block import *
from .renderer_hitbox import RendererHitbox


class RendererWorld:
    @staticmethod
    def render(screen, world, camera=None, render_hitbox=True):
        for entity in world.entities:
            RendererEntity.render(screen, entity, camera)

            if render_hitbox:
                RendererHitbox.render(screen, entity.hitbox, camera=camera)
