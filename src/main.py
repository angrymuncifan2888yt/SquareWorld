import pygame
import sys
from world import World
from world.entity import *
from world.block import *
from core import Position, Camera, Direction
from assets import Sound
from assets import Fonts, Sprites
from common import const
from command import TypingField
from hud import HUD
from renderer.other import RendererWorld
from user_input import user_input
import os


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        Fonts.init(os.path.join("assets", "fonts", "GameFont.ttf"))
        Sound.init()

        self.screen = pygame.display.set_mode(const.WINDOW_SIZE)
        Sprites.init()
        pygame.display.set_caption("Square World")
        self.clock = pygame.time.Clock()

        self.camera = Camera(Position(0, 0), 1200, 800)
        self.world = World(None)
        self.world.player = EntityPlayer(self.world, Position(0, 100))
        self.world.add_entity(EntityTriangle(self.world, Position(400, 400)))
        self.world.add_entity(EntityMedkit(self.world, Position(100, 400)))
        self.world.add_entity(EntityBomb(self.world, Position(400, -400)))
        self.world.add_block(ObsidianBlock(self.world, Position(0, 0)))

        self.free_cam = False
        self.debug = False

        # Command
        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False

        # HUD
        self.hud = HUD(self.world)

        self.blocks = [GrassBlock, StoneBlock, ObsidianBlock]
        self.current_block_index = 0

    def process_world(self, delta: float):
        self.world.delta = delta
        if not self.free_cam:
            self.camera.center_on(
                self.world.player.hitbox.position,
                self.world.player.hitbox.width,
                self.world.player.hitbox.height
            )
        self.world.update()
        RendererWorld.render(self.screen, self.world, self.camera, self.debug)

    def mainloop(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))

            delta = self.clock.tick(60) / 1000
            pg_event = pygame.event.get()

            self.process_world(delta)

            if self.hud.is_on:
                self.hud.update(pg_event, delta, self.world, self.debug, self.blocks[self.current_block_index])
                self.hud.render(self.screen, self.clock, self.camera, self.debug)

            user_input(self, pg_event, delta)

if __name__ == "__main__":
    game = Game()
    game.mainloop()
