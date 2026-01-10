import pygame
from ..entity import Entity
from ..other import EntityPlayer
from assets import calculate_sound_volume, AdvancedSound


class EntityNextbot(Entity):    
    def __init__(self, world, position, width, height, ambience: AdvancedSound, speed=1000, turn_speed=2, creation_params=None):
        # Initialize the Nextbot entity with given size and movement parameters
        super().__init__(world, position, width, height, creation_params)
        self.speed = speed  # Movement speed of the bot
        self.turn_speed = turn_speed  # How fast the bot can change direction
        self.velocity = pygame.Vector2(1, 0)  # Current movement direction vector
        self.ambience = ambience  # Ambient sound associated with this bot

    def update(self, delta):
        # Play ambient sound with volume based on distance to player (if on)
        if self.world.nextbot_sound:
            volume = calculate_sound_volume(self.position, self.world.player.position, 800)
            self.ambience.play_looped(volume)

        # Move the bot towards the player if AI is enabled
        if self.world.nextbot_ai:
            player_pos = pygame.Vector2(self.world.player.position.x,
                                        self.world.player.position.y)
            bot_pos = pygame.Vector2(self.position.x, self.position.y)

            direction = (player_pos - bot_pos)
            distance = direction.length()
            if distance == 0:
                return  # Avoid division by zero if bot is exactly on player

            direction = direction.normalize()  # Get unit direction vector

            # Smoothly interpolate velocity toward desired direction based on turn_speed
            t = max(0, min(self.turn_speed * delta, 1))
            self.velocity = self.velocity.lerp(direction, t)

            # Update bot position based on velocity, speed, and delta time
            self.position.x += self.velocity.x * self.speed * delta
            self.position.y += self.velocity.y * self.speed * delta

    def onEntityCollision(self, entity):
        # If bot collides with player, instantly kill the player
        if isinstance(entity, EntityPlayer):
            entity.kill()

    def stop_sound(self):
        # Stop the ambient sound
        self.ambience.stop()
