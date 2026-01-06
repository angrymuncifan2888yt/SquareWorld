class Scene:
    def __init__(self, scene_manager, id):
        self.id = id
        self.scene_manager = scene_manager

    def input(self, *args, **kwargs):
        pass

    def logic(self, *args, **kwargs):
        pass

    def draw(self, screen):
        pass