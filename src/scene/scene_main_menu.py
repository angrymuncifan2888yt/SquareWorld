from .scene import Scene
from .scene_list import SceneList


class SceneMainMenu(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager, SceneList.MAIN_MENU)
        