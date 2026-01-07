from .renderer_entity_player import RendererEntityPlayer
from .renderer_entity_triangle import RendererEntityTriangle
from .renderer_entity_medkit import RendererEntityMedkit
from .renderer_entity_bomb import RendererEntityBomb
from .nextbot import *
from world.entity import *
from world.entity.nextbot import *


class RendererEntity:
    render_list = {
        EntityPlayer: RendererEntityPlayer,
        EntityBomb: RendererEntityBomb,
        EntityTriangle: RendererEntityTriangle,
        EntityMedkit: RendererEntityMedkit,
        NextbotAsya: RendererNextbotAsya,
        NextbotAngryMunci: RendererNextbotAngryMunci,
        NextbotSuperMunci: RendererNextbotSuperMunci
    }
    @staticmethod
    def render(screen, entity, camera=None):
        RendererEntity.render_list[type(entity)].render(screen, entity, camera)
        