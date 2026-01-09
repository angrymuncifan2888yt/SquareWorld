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
        # Initialize the main game scene
        super().__init__(scene_manager, SceneList.GAME)

        # Camera setup
        self.camera = Camera(Position(0, 0), 1200, 800)

        # Initialize the game world and add entities
        self.world = World(None)
        self.world.player = EntityPlayer(self.world, Position(0, 100))  # Player entity
        self.world.add_entity(EntityTriangle(self.world, Position(400, 400)))  # Enemy triangle
        self.world.add_entity(EntityMedkit(self.world, Position(100, 400)))   # Healing item
        self.world.add_entity(EntityBomb(self.world, Position(400, -400)))    # Bomb
        self.world.add_entity(ObsidianBlock(self.world, Position(0, 0)))      # Block
        # self.world.add_entity(NextbotAngryMunci(self.world, Position(1000, 1000)))  # Optional Nextbot enemy

        self.free_cam = False  # Flag for free camera mode
        self.debug = False     # Flag for debug info

        # Typing command system
        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False

        # HUD
        self.hud = HUD(self.world)

        # Available block types and current selection
        self.blocks = [GrassBlock, StoneBlock, ObsidianBlock]
        self.current_block_index = 0
        self.clock = None

    def input(self, *args, **kvargs):
        # Handle user input events using the shared user_input function
        user_input(self, kvargs["pg_event"], kvargs["delta"])

    def logic(self, *args, **kvargs):
        # Main logic update for the scene
        self.clock = kvargs["clock"]

        # Update world
        self.world.delta = kvargs["delta"]
        if not self.free_cam:
            # Center camera on the player unless free_cam is enabled
            self.camera.center_on(
                self.world.player.hitbox.position,
                self.world.player.hitbox.width,
                self.world.player.hitbox.height
            )
        self.world.update()  # Update all entities in the world

        # Update HUD if enabled
        if self.hud.is_on:
            self.hud.update(
                kvargs["pg_event"], 
                kvargs["delta"], 
                self.world, 
                self.debug, 
                self.blocks[self.current_block_index]
            )

    def draw(self, screen, **kvargs):
        # Render the game world
        RendererWorld.render(screen, self.world, self.camera, self.debug)

        # Render the HUD on top of the world
        self.hud.render(screen, self.clock, self.camera, self.debug)
