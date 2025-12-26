import os
import pygame


class Sound:
    SOUND_DAMAGE = None
    SOUND_HEAL = None
    @classmethod
    def init(cls):
        cls.SOUND_HEAL = pygame.mixer.Sound(os.path.join("assets", "sound", "heal.mp3"))
        cls.SOUND_DAMAGE = pygame.mixer.Sound(os.path.join("assets", "sound", "damage.mp3"))
    @classmethod
    def damage(cls):
        cls.SOUND_DAMAGE.play()
    
    @classmethod
    def heal(cls):
        cls.SOUND_HEAL.play()
