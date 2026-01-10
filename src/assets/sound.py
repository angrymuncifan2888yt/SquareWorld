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

    def play_looped(self, volume: float):
        final_volume = self.base_volume * volume

        if final_volume <= 0:
            self.stop()
            return

        if self.channel is None or not self.channel.get_busy():
            self.channel = pygame.mixer.find_channel(False)
            if self.channel is None:
                return
            self.channel.play(self.sound, loops=-1)

        self.channel.set_volume(final_volume)

    def stop(self):
        if self.channel:
            self.channel.stop()
            self.channel = None

    def play_once(self, volume: float = 1.0):
        final_volume = self.base_volume * volume
        if final_volume <= 0:
            return

        channel = pygame.mixer.find_channel(False)
        if channel is None:
            return

        channel.set_volume(final_volume)
        channel.play(self.sound)


class SoundStorage:
    DAMAGE = None
    HEAL = None
    EXPLOSION = None
    BREAKING = None
    ANGRY_MUNCI_AMBIENCE = None
    ASYA_AMBIENCE = None
    SUPER_MUNCI_AMBIENCE = None
    KING_MUNCI_ROAR = None

    @classmethod
    def init(cls):
        cls.DAMAGE = pygame.mixer.Sound("assets/sound/damage.mp3")
        cls.HEAL = pygame.mixer.Sound("assets/sound/heal.mp3")
        cls.EXPLOSION = pygame.mixer.Sound("assets/sound/explosion.mp3")
        cls.BREAKING = pygame.mixer.Sound("assets/sound/breaking.mp3")
        cls.ANGRY_MUNCI_AMBIENCE = pygame.mixer.Sound("assets/sound/angry_munci_ambience.mp3")
        cls.ASYA_AMBIENCE = pygame.mixer.Sound("assets/sound/asya_ambience.mp3")
        cls.SUPER_MUNCI_AMBIENCE = pygame.mixer.Sound("assets/sound/super_munci_ambience.mp3")
        cls.KING_MUNCI_ROAR = pygame.mixer.Sound("assets/sound/king_munci_roar.mp3")