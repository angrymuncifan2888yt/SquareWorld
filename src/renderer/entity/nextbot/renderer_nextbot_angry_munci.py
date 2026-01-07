import pygame
from assets import Sprites


class RendererNextbotAngryMunci:
    @staticmethod
    def render(screen, nextbot, camera=None):
        nextbot_pos = camera.get_screen_position(nextbot.position) if camera else nextbot.position

        screen.blit(Sprites.ANGRY_MUNCI_TEXTURE, nextbot_pos.to_tuple())
