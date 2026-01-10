from assets import Sprites


class RendererNextbotKingMunci:
    @staticmethod
    def render(screen, nextbot, camera=None):
        nextbot_pos = camera.get_screen_position(nextbot.position) if camera else nextbot.position

        screen.blit(Sprites.KING_MUNCI_TEXTURE, nextbot_pos.to_tuple())
