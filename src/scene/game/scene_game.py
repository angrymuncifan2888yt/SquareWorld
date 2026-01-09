from ..scene import Scene
from ..scene_list import SceneList
from core import Camera, Position
from world import World
from world.other import *
from world.nextbot import *
from world.block import *
from command import TypingField
from assets import Fonts
from .hud import HUD
from .user_input import user_input
from renderer.other import RendererWorld


class SceneGame(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager, SceneList.GAME)
        self.camera = Camera(Position(0, 0), 1200, 800)

        # World
        self.world = World(None)
        self.world.player = EntityPlayer(self.world, Position(0, 100))
        self.world.add_entity(EntityTriangle(self.world, Position(400, 400)))
        self.world.add_entity(EntityMedkit(self.world, Position(100, 400)))
        self.world.add_entity(EntityBomb(self.world, Position(400, -400)))
        self.world.add_entity(ObsidianBlock(self.world, Position(0, 0)))
        # self.world.add_entity(NextbotAngryMunci(self.world, Position(1000, 1000)))

        self.free_cam = False
        self.debug = False

        # Command
        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False

        # HUD
        self.hud = HUD(self.world)

        self.blocks = [GrassBlock, StoneBlock, ObsidianBlock]
        self.current_block_index = 0
        self.clock = None

    def input(self, *args, **kvargs):
         user_input(self, kvargs["pg_event"], kvargs["delta"])

    def logic(self, *args, **kvargs):
        self.clock = kvargs["clock"]

        # World
        self.world.delta = kvargs["delta"]
        if not self.free_cam:
            self.camera.center_on(
                self.world.player.hitbox.position,
                self.world.player.hitbox.width,
                self.world.player.hitbox.height
            )
        self.world.update()


        # HUD
        if self.hud.is_on:
            self.hud.update(kvargs["pg_event"], kvargs["delta"], self.world, self.debug, self.blocks[self.current_block_index])

    def draw(self, screen, **kvargs):
        RendererWorld.render(screen, self.world, self.camera, self.debug)
        self.hud.render(screen, self.clock, self.camera, self.debug)

           