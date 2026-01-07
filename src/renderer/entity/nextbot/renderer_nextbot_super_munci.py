from assets import Sprites


class RendererNextbotSuperMunci:
    @staticmethod
    def render(screen, nextbot, camera=None):
        nextbot_pos = camera.get_screen_position(nextbot.position) if camera else nextbot.position

        screen.blit(Sprites.SUPER_MUNCI_TEXTURE, nextbot_pos.to_tuple())
