from command import TypingField
from common import const
from core import Camera
import pygame


class RendererTypingField:
    @staticmethod
    def render(screen: pygame.Surface, typing_field: TypingField, camera: Camera=None):
        # Background
        surface_background = pygame.Surface((const.WINDOW_SIZE[0] + 100, 80))
        surface_background.fill((50, 50, 50))
        screen.blit(surface_background, (typing_field.position.x - 20, typing_field.position.y - 15))

        # Text
        typing_field_pos = camera.get_screen_position(typing_field.position) if camera else typing_field.position

        text_surface = typing_field.font.render(typing_field.text, True, (255, 255, 255))
        screen.blit(text_surface, (typing_field_pos.x, typing_field_pos.y))

        # Text cursor
        if typing_field.text_cursor.is_visible:
            cursor_pos = camera.get_screen_position(typing_field.text_cursor.position) if camera else typing_field.text_cursor.position
            surface = pygame.Surface((typing_field.text_cursor.hitbox.width,
                                    typing_field.text_cursor.hitbox.height))
            surface.fill((155, 155, 155))
            screen.blit(surface, (cursor_pos.x, cursor_pos.y))
