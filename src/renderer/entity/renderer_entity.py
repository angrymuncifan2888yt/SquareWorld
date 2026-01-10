from .other import RendererEntityTriangle, RendererEntityBomb, RendererEntityMedkit, RendererEntityPlayer
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
        NextbotAsya: RendererNextbotAsya,
        NextbotAngryMunci: RendererNextbotAngryMunci,
        NextbotSuperMunci: RendererNextbotSuperMunci,
        ObsidianBlock: RendererBlock,
        StoneBlock: RendererBlock,
        GrassBlock: RendererBlock,
    }
    @staticmethod
    def render(screen, entity, camera=None):
        RendererEntity.render_list[type(entity)].render(screen, entity, camera)
        