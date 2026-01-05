import pygame
import os


class Sprites:
    BREAKING_STAGES = []

    @classmethod
    def init(cls):
        cls.BREAKING_STAGES = [
            pygame.transform.scale(
                pygame.image.load(os.path.join("assets", "img", "block_breaking.png")).convert_alpha(),
                (100, 100)),
            pygame.transform.scale(
                pygame.image.load(os.path.join("assets", "img", "block_breaking2.png")).convert_alpha(),
                (100, 100))]