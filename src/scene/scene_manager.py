class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes[scene.id] = scene

    def set_scene(self, id):
        self.current_scene = self.scenes[id]

    def input_current_scene(self, *args, **kwargs):
        self.current_scene.input(*args, **kwargs)

    def logic_current_scene(self, *args, **kwargs):
        self.current_scene.logic(*args, **kwargs)

    def draw_current_scene(self, screen, *args, **kvargs):
        self.current_scene.draw(screen, *args, **kvargs)