from .scene import Scene
from .scene_list import SceneList
from graphics import Text, Button
from assets import Fonts
from core import Position
import const
from renderer.graphics import RendererText, RendererButton
import pygame


class SceneMainMenu(Scene):
    def __init__(self, scene_manager):
        # Initialize the main menu scene
        super().__init__(scene_manager, SceneList.MAIN_MENU)

        # Title text at the top of the screen
        self.text_title = Text("SquareWorld", Position(0, 10), Fonts.FONT_100)
        self.text_title.center_by_x(const.WINDOW_SIZE[0])

        # Play button in the center
        self.button_play = Button(Text("Press enter to play", Position(0, 0), Fonts.FONT_30), Position(100, 120))
        self.button_play.center_by_x(const.WINDOW_SIZE[0])

    def input(self, *args, **kwargs):
        # Handle user input events
        pg_event = kwargs["pg_event"]
        
        # Check if the play button is clicked
        if self.button_play.isClicked(pg_event):
            self.scene_manager.set_scene(SceneList.GAME)

        # Check if Enter key is pressed to start the game
        for event in pg_event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.scene_manager.set_scene(SceneList.GAME)

    def draw(self, screen):
        # Draw the title and play button on the screen
        RendererText.render(screen, self.text_title)
        RendererButton.render(screen, self.button_play)
