from core import Hitbox


class Entity:
    def __init__(self, world, position, width, height, creation_params: dict = None):
        super().__init__()
        self.world = world
        self.hitbox = Hitbox(position, width, height)

        if isinstance(creation_params, dict):
            if creation_params.get("width"):
                self.hitbox.width = int(creation_params["width"])
            if creation_params.get("height"):
                self.hitbox.height = int(creation_params["height"])

    def update(self, delta: float):
        pass

    @property
    def position(self):
        return self.hitbox.position

    @position.setter
    def position(self, value):
        self.hitbox.position = value

    def onEntityCollision(self, entity):
        pass

    def onBombExplosionCollision(self, bomb):
        self.destroy()

    def onBlockCollision(self, block):
        self.hitbox.handle_collision(block.hitbox)

    def destroy(self):
        self.world.remove_entity(self)

    def stop_sound(self):
        pass