import pygame
from .renderer_text import RendererText
from core import Camera


class RendererButton:
    @staticmethod
    def render(screen, button, camera: Camera=None):
        button_pos = camera.get_screen_position(button.position) if camera else button.position
        surf = pygame.Surface((button.hitbox.width, button.hitbox.height))
        if button.is_mouse_in_button():
            surf.fill(button.hover_color)
        
        else:
            surf.fill(button.color)
        screen.blit(surf, button_pos.to_tuple())
        RendererText.render(screen, button.text, camera)
