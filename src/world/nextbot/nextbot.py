import pygame
from ..entity import Entity
from ..other import EntityPlayer
import pygame
from assets import calculate_sound_volume, AdvancedSound


class EntityNextbot(Entity):    
    def __init__(self, world, position, width, height, ambience: AdvancedSound, speed=1000, turn_speed=2, creation_params=None):
        super().__init__(world, position, width, height, creation_params)
        self.speed = speed
        self.turn_speed = turn_speed
        self.velocity = pygame.Vector2(1, 0)
        self.ambience = ambience

    def update(self, delta):
        if self.world.nextbot_ai:
            player_pos = pygame.Vector2(self.world.player.position.x,
                                        self.world.player.position.y)
            bot_pos = pygame.Vector2(self.position.x, self.position.y)

            direction = (player_pos - bot_pos)
            distance = direction.length()
            if distance == 0:
                return

            direction = direction.normalize()

            t = max(0, min(self.turn_speed * delta, 1))
            self.velocity = self.velocity.lerp(direction, t)

            self.position.x += self.velocity.x * self.speed * delta
            self.position.y += self.velocity.y * self.speed * delta
        
        self.ambience.play_looped(calculate_sound_volume(self.position, self.world.player.position, 800))

    def onEntityCollision(self, entity):
        if isinstance(entity, EntityPlayer):
            entity.kill()

    def stop_sound(self):
        self.ambience.stop()
