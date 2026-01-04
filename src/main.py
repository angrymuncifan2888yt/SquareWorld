import pygame
import sys
from world import World
from world.entity import *
from world.block import *
from core import Position, Camera, Direction
from assets import Sound
from assets import Fonts
from common import Const
from command import TypingField
from hud import HUD
from renderer.other import RendererWorld
import os


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        Fonts.init(os.path.join("assets", "fonts", "GameFont.ttf"))
        Sound.init()

        self.screen = pygame.display.set_mode((Const.WINDOW_WIDTH, 800))
        pygame.display.set_caption("Square World")
        self.clock = pygame.time.Clock()

        self.camera = Camera(Position(0, 0), 1200, 800)
        self.world = World(EntityPlayer(Position(0, 100)))
        self.world.add_entity(EntityTriangle(Position(400, 400)))
        self.world.add_entity(EntityPlatform(Position(-100, 0)))
        self.world.add_entity(EntityMedkit(Position(100, 400)))
        self.world.add_entity(EntityBomb(Position(400, -400)))
        self.world.add_block(ObsidianBlock(Position(0, 0)))

        self.free_cam = False
        self.debug = False

        # Command
        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False

        # HUD
        self.hud = HUD(self.world)

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
                self.hud.process_hud(self.screen, self.clock, self.camera, pg_event, delta, self.world, self.debug)

            keys_pressed = pygame.key.get_pressed()

            if not self.hud.do_type:
                if keys_pressed[pygame.K_a]:
                    self.world.player.position.move(Direction.LEFT, Const.PLAYER_SPEED, self.world.delta)

                if keys_pressed[pygame.K_d]:
                    self.world.player.position.move(Direction.RIGHT, Const.PLAYER_SPEED, self.world.delta)

                if keys_pressed[pygame.K_w]:
                    self.world.player.position.move(Direction.TOP, Const.PLAYER_SPEED, self.world.delta)

                if keys_pressed[pygame.K_s]:
                    self.world.player.position.move(Direction.DOWN, Const.PLAYER_SPEED, self.world.delta)

                # Camera movement
                if keys_pressed[pygame.K_j]:  # KJ!!!!!
                    self.camera.position.move(Direction.LEFT, Const.CAMERA_SPEED, delta)
                    self.free_cam = True

                if keys_pressed[pygame.K_l]:
                    self.camera.position.move(Direction.RIGHT, Const.CAMERA_SPEED, delta)
                    self.free_cam = True

                if keys_pressed[pygame.K_i]:
                    self.camera.position.move(Direction.TOP, Const.CAMERA_SPEED, delta)
                    self.free_cam = True

                if keys_pressed[pygame.K_k]:
                    self.camera.position.move(Direction.DOWN, Const.CAMERA_SPEED, delta)
                    self.free_cam = True

            for event in pg_event:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.free_cam = False

                    elif event.key == pygame.K_F1:
                        self.hud.is_on = not self.hud.is_on
                    
                    elif event.key == pygame.K_TAB:
                        self.debug = not self.debug

                    elif event.key == pygame.K_SLASH:
                        if self.hud.is_on:
                            self.hud.do_type = not self.hud.do_type

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos

                        world_x = mouse_x + self.camera.position.x
                        world_y = mouse_y + self.camera.position.y

                        self.world.add_block(
                            GrassBlock(
                                Position(world_x, world_y)
                            )
                        )

                    if event.button == 3:
                        print("Break")


if __name__ == "__main__":
    game = Game()
    game.mainloop()
