class Scene:
    def __init__(self, scene_manager, id):
        self.id = id
        self.scene_manager = scene_manager

    def update(self, *args, **kwargs):
        pass

    def render(self, screen):
        pass