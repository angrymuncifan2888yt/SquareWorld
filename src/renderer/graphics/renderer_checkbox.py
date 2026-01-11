import pygame


class RendererCheckBox:
    @staticmethod
    def render(screen: pygame.Surface, checkbox, camera=None):
        pos = camera.get_screen_position(checkbox.position) if camera else checkbox.position
        surf = pygame.Surface((checkbox.hitbox.width, checkbox.hitbox.height))
        color = (0, 255, 0) if checkbox.is_on else (255, 0, 0)
        surf.fill(color)
        screen.blit(surf, pos.to_tuple())
