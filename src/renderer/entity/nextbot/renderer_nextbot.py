class RendererNextbot:
    @staticmethod
    def render(screen, nextbot, camera=None):
        nextbot_pos = camera.get_screen_position(nextbot.position) if camera else nextbot.position

        screen.blit(nextbot.image(), nextbot_pos.to_tuple())
