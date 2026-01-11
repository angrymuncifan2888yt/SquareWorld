from world.nextbot import *
from .renderer_nextbot_king_munci import RendererNextbotKingMunci


class BaseRendererNextbot:
    @staticmethod
    def render(screen, nextbot, camera=None):
        nextbot_pos = camera.get_screen_position(nextbot.position) if camera else nextbot.position
        screen.blit(nextbot.image(), nextbot_pos.to_tuple())



class RendererNextbot:
    render_list = {
        NextbotAsya: BaseRendererNextbot,
        NextbotAngryMunci: BaseRendererNextbot,
        NextbotSuperMunci: BaseRendererNextbot,
        NextbotKingMunci: RendererNextbotKingMunci
    }
    @staticmethod
    def render(screen, nextbot, camera=None):
        RendererNextbot.render_list[type(nextbot)].render(screen, nextbot, camera)