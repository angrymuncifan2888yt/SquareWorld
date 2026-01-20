from .text import Text
from core.timer import Timer
import pygame

class TempText(Text):
    def __init__(self, text: str, position,
                 font: pygame.font.Font,
                 color: tuple[int, int, int]=(255, 255, 255),
                 timer: Timer = Timer(3)):
        super().__init__(text, position, font, color)
        self.timer = timer
        self.is_visible = False
    
    def update(self, delta):
        if self.is_visible:
            self.timer.update(delta)

        if self.timer.finished:
            self.hide()

    def show(self):
        self.is_visible = True
        self.timer.reset()
    
    def hide(self):
        self.is_visible = False
    
    def render(self, surface, camera=None):
        if self.is_visible:
            super().render(surface, camera)