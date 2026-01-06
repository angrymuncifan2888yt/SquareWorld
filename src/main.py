import pygame
from world import World
from world.entity import *
from world.block import *
from core import Position, Camera
from assets import Sound
from assets import Fonts, Sprites
from common import const
from command import TypingField
from renderer.other import RendererWorld
from scene.game import SceneGame
from scene import SceneManager
import os
import sys


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

        self.scene_manager = SceneManager()
        self.scene_manager.add_scene(SceneGame(self.scene_manager))
        self.scene_manager.set_scene("game")

    def mainloop(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))

            delta = self.clock.tick(60) / 1000
            pg_event = pygame.event.get()

            self.scene_manager.input_current_scene(delta=delta, pg_event=pg_event)
            self.scene_manager.logic_current_scene(delta=delta, pg_event=pg_event, clock=self.clock)
            self.scene_manager.draw_current_scene(self.screen)
    
            for event in pg_event:
                if event.type == pygame.QUIT:
                    sys.exit(0)

if __name__ == "__main__":
    game = Game()
    game.mainloop()
