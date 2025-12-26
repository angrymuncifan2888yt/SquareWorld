import pygame


class Fonts:
    FONT_10 = None
    FONT_20 = None
    FONT_30 = None
    FONT_40 = None
    FONT_50 = None
    FONT_60 = None
    FONT_70 = None
    FONT_80 = None
    FONT_90 = None
    FONT_100 = None
    FONT_200 = None

    @classmethod
    def init(cls, font: str = None):
        cls.FONT_10 = pygame.font.Font(font, 10)
        cls.FONT_20 = pygame.font.Font(font, 20)
        cls.FONT_30 = pygame.font.Font(font, 30)
        cls.FONT_40 = pygame.font.Font(font, 40)
        cls.FONT_50 = pygame.font.Font(font, 50)
        cls.FONT_60 = pygame.font.Font(font, 60)
        cls.FONT_70 = pygame.font.Font(font, 70)
        cls.FONT_80 = pygame.font.Font(font, 80)
        cls.FONT_90 = pygame.font.Font(font, 90)
        cls.FONT_100 = pygame.font.Font(font, 100)
        cls.FONT_200 = pygame.font.Font(font, 200)
