from .scene import Scene
from .scene_list import SceneList
from graphics import Text, Button, CheckBox, UiManager
from assets import Fonts
from core import Position
import const
import pygame


class SceneMainMenu(Scene):
    def __init__(self, scene_manager):
        # Initialize the main menu scene
        super().__init__(scene_manager, SceneList.MAIN_MENU)

        self.ui = UiManager()

        # Title text at the top of the screen
        self.text_title = Text("SquareWorld", Position(0, 10), Fonts.FONT_100)
        self.text_title.center_by_x(const.WINDOW_SIZE[0])

        # Play button in the center
        self.button_play = Button(Text("Press enter to play", Position(0, 0), Fonts.FONT_30), Position(100, 120), self._button_play_clicked)
        self.button_play.center_by_x(const.WINDOW_SIZE[0])

        # Music checkbox
        self.checkbox_music = CheckBox(Position(400, 250), self._music_checkbox_clicked)
        self.checkbox_music.is_on = True
        self.text_music = Text(f"Music: {self.checkbox_music.is_on}", Position(550, 275), Fonts.FONT_30)
        self.ui.add_ui_object(self.text_title)
        self.ui.add_ui_object(self.button_play)
        self.ui.add_ui_object(self.checkbox_music)
        self.ui.add_ui_object(self.text_music)

    def _music_checkbox_clicked(self):
        self.text_music.text = f"Music: {self.checkbox_music.is_on}"
        if self.checkbox_music.is_on:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

    def _button_play_clicked(self):
        self.scene_manager.set_scene(SceneList.GAME)

    def update(self, *args, **kwargs):
        # Handle user input events
        pg_event = kwargs["pg_event"]
        delta = kwargs["delta"]

        # Check if Enter key is pressed to start the game
        for event in pg_event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.scene_manager.set_scene(SceneList.GAME)

        self.ui.update(delta, pg_event)
     
    def render(self, screen):
        # Draw the title and play button on the screen
        self.ui.render(screen)