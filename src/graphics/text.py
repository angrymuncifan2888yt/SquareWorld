from core import Position
import pygame


class Text:
    def __init__(self, text: str, position: Position,
                 font: pygame.font.Font, color: tuple[int, int, int]=(255, 255, 255)):
        self.text = text
        self.position = position
        self.font = font
        self.color = color

    def center_by_x(self, screen_width: int):
        text_width = self.font.size(self.text)[0]
        self.position.x = (screen_width - text_width) / 2

    def center_in_hitbox(self, hitbox):
        w, h = self.font.size(self.text)
        self.position.x = hitbox.position.x + (hitbox.width - w) / 2
        self.position.y = hitbox.position.y + (hitbox.height - h) / 2
