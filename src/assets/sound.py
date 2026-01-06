import os
import pygame


class Sound:
    SOUND_DAMAGE = None
    SOUND_HEAL = None
    SOUND_EXPLOSION = None
    SOUND_BREAKING = None
    @classmethod
    def init(cls):
        cls.SOUND_HEAL = pygame.mixer.Sound(os.path.join("assets", "sound", "heal.mp3"))
        cls.SOUND_DAMAGE = pygame.mixer.Sound(os.path.join("assets", "sound", "damage.mp3"))
        cls.SOUND_EXPLOSION = pygame.mixer.Sound(os.path.join("assets", "sound", "explosion.mp3"))
        cls.SOUND_BREAKING = pygame.mixer.Sound(os.path.join("assets", "sound", "breaking.mp3"))
    @classmethod
    def damage(cls):
        cls.SOUND_DAMAGE.play()
    
    @classmethod
    def heal(cls):
        cls.SOUND_HEAL.play()

    @classmethod
    def explode(cls):
        cls.SOUND_EXPLOSION.play()

    @classmethod
    def breaking(cls):
        cls.SOUND_BREAKING.play()
