import pygame
from ..entity import Entity
from ..entity_player import EntityPlayer

class EntityNextbot(Entity):
    def __init__(self, world, position, width, height, speed=1000, turn_speed=2, creation_params=None):
        super().__init__(world, position, width, height, creation_params)
        self.speed = speed
        self.turn_speed = turn_speed
        self.velocity = pygame.Vector2(1, 0)

    def update(self, delta):
        player_pos = pygame.Vector2(self.world.player.position.x,
                                    self.world.player.position.y)
        bot_pos = pygame.Vector2(self.position.x, self.position.y)

        direction = (player_pos - bot_pos)
        distance = direction.length()
        if distance == 0:
            return

        direction = direction.normalize()

        self.velocity = self.velocity.lerp(direction, self.turn_speed * delta)

        self.position.x += self.velocity.x * self.speed * delta
        self.position.y += self.velocity.y * self.speed * delta

    def onEntityCollision(self, entity):
        if isinstance(entity, EntityPlayer):
            entity.kill()
