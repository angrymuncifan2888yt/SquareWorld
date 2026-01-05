from .renderer_entity_player import RendererEntityPlayer
from .renderer_entity_triangle import RendererEntityTriangle
from .renderer_entity_medkit import RendererEntityMedkit
from .renderer_entity_bomb import RendererEntityBomb
from world.entity import *


class RendererEntity:
    render_list = {
        EntityPlayer: RendererEntityPlayer,
        EntityBomb: RendererEntityBomb,
        EntityTriangle: RendererEntityTriangle,
        EntityMedkit: RendererEntityMedkit
    }
    @staticmethod
    def render(screen, entity, camera=None):
        RendererEntity.render_list[type(entity)].render(screen, entity, camera)
        