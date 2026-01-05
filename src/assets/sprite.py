import pygame
import os
from common import const


class Sprites:
    BREAKING_STAGES = []
    GRASS_BLOCK_TEXTURE = None
    OBSIDIAN_BLOCK_TEXTURE = None

    @classmethod
    def init(cls):
        cls.GRASS_BLOCK_TEXTURE = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "img", "grass.jpg")).convert_alpha(),
            const.BLOCK_SIZE)
        cls.OBSIDIAN_BLOCK_TEXTURE = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "img", "obsidian.jpg")).convert_alpha(),
            const.BLOCK_SIZE)
        cls.STONE_BLOCK_TEXTURE = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "img", "stone.jpg")).convert_alpha(),
            const.BLOCK_SIZE)

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