import pygame


class RendererNextbotKingMunci:
    @staticmethod
    def render(screen, nextbot, camera=None):
        nextbot_pos = camera.get_screen_position(nextbot.position) if camera else nextbot.position

        if nextbot.is_enraged:
            radius = 140
            aura = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(aura, (200, 30, 30, 80), (radius, radius), radius)

            x = nextbot_pos.x + nextbot.hitbox.width // 2 - radius
            y = nextbot_pos.y + nextbot.hitbox.height // 2 - radius
            screen.blit(aura, (x, y))

        screen.blit(nextbot.image(), nextbot_pos.to_tuple())
