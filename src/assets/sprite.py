import pygame
import os
from common import const


class Sprites:
    BREAKING_STAGES = []

    @classmethod
    def init(cls):
        cls.BREAKING_STAGES = [
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_0.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_1.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_2.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_3.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_4.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_5.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_6.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_7.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_8.png")),
            pygame.image.load(os.path.join("assets", "img", "destroy_stage_9.png")),
            ]
        counter = 0
        for stage in cls.BREAKING_STAGES:
            cls.BREAKING_STAGES[counter] = pygame.transform.scale(stage, const.BLOCK_SIZE)
            counter += 1