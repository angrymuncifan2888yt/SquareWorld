import os
import pygame
import math


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
    def explode(cls, source_pos, listener_pos):
        Sound.play_sound_at(cls.SOUND_EXPLOSION, source_pos, listener_pos, 1500)

    @classmethod
    def breaking(cls):
        cls.SOUND_BREAKING.play()

    @staticmethod
    def play_sound_at(sound: pygame.mixer.Sound, source_pos, listener_pos, max_distance):
        dx = source_pos.x - listener_pos.x
        dy = source_pos.y - listener_pos.y
        distance = math.hypot(dx, dy)

        if distance >= max_distance:
            return

        volume = 1.0 - (distance / max_distance)
        volume = max(0.0, min(1.0, volume))

        sound.set_volume(volume)
        sound.play()