class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes[scene.id] = scene

    def set_scene(self, id):
        self.current_scene = self.scenes[id]

    def update_current_scene(self, *args, **kwargs):
        self.current_scene.update(*args, **kwargs)

    def render_current_scene(self, screen, *args, **kvargs):
        self.current_scene.render(screen, *args, **kvargs)