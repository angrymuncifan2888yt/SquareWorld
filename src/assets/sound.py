import os
import pygame
import math


def calculate_sound_volume(source_pos, listener_pos, max_distance):
    dx = source_pos.x - listener_pos.x
    dy = source_pos.y - listener_pos.y
    distance = math.hypot(dx, dy)

    if distance >= max_distance:
        return 0.0

    volume = 1.0 - (distance / max_distance)
    return max(0.0, min(1.0, volume))


class AdvancedSound:
    def __init__(self, sound: pygame.mixer.Sound, base_volume: float = 1.0):
        self.sound = sound
        self.base_volume = max(0.0, min(1.0, base_volume))
        self.channel: pygame.mixer.Channel | None = None

    def set_base_volume(self, volume: float):
        self.base_volume = max(0.0, min(1.0, volume))

    def play_once(self, volume: float = 1.0):
        final_volume = self.base_volume * volume
        if final_volume <= 0:
            return
        self.sound.set_volume(final_volume)
        self.sound.play()

    def play_looped(self, volume: float = 1.0):
        final_volume = self.base_volume * volume

        if final_volume <= 0:
            self.stop()
            return

        if self.channel is None or not self.channel.get_busy():
            self.channel = self.sound.play(loops=-1)

        if self.channel:
            self.channel.set_volume(final_volume)

    def stop(self):
        if self.channel:
            self.channel.stop()
            self.channel = None


class Sound:
    DAMAGE: AdvancedSound = None
    HEAL: AdvancedSound = None
    EXPLOSION: AdvancedSound = None
    BREAKING: AdvancedSound = None
    ANGRY_MUNCI_AMBIENCE: AdvancedSound = None
    ASYA_AMBIENCE: AdvancedSound = None
    SUPER_MUNCI_AMBIENCE: AdvancedSound = None

    @classmethod
    def init(cls):
        cls.DAMAGE = AdvancedSound(
            pygame.mixer.Sound("assets/sound/damage.mp3")
        )
        cls.HEAL = AdvancedSound(
            pygame.mixer.Sound("assets/sound/heal.mp3")
        )
        cls.EXPLOSION = AdvancedSound(
            pygame.mixer.Sound("assets/sound/explosion.mp3")
        )
        cls.BREAKING = AdvancedSound(
            pygame.mixer.Sound("assets/sound/breaking.mp3")
        )
        cls.ANGRY_MUNCI_AMBIENCE = AdvancedSound(
            pygame.mixer.Sound("assets/sound/angry_munci_ambience.mp3")
        )
        cls.ASYA_AMBIENCE = AdvancedSound(
            pygame.mixer.Sound("assets/sound/asya_ambience.mp3")
        )
        cls.SUPER_MUNCI_AMBIENCE = AdvancedSound(
            pygame.mixer.Sound("assets/sound/super_munci_ambience.mp3")
        )