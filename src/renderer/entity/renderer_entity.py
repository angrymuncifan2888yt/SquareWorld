from .other import *
from .nextbot import *
from .block import RendererBlock
from world.other import *
from world.nextbot import *
from world.block import *


class RendererEntity:
    render_list = {
        EntityPlayer: RendererEntityPlayer,
        EntityBomb: RendererEntityBomb,
        EntityTriangle: RendererEntityTriangle,
        EntityMedkit: RendererEntityMedkit,
        NextbotAsya: RendererNextbot,
        NextbotAngryMunci: RendererNextbot,
        NextbotSuperMunci: RendererNextbot,
        NextbotKingMunci: RendererNextbot,
        ObsidianBlock: RendererBlock,
        StoneBlock: RendererBlock,
        GrassBlock: RendererBlock,
        EntityBullet: RendererEntityBullet
    }
    @staticmethod
    def render(screen, entity, camera=None):
        RendererEntity.render_list[type(entity)].render(screen, entity, camera)
        