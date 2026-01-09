from core import Hitbox


class Entity:
    def __init__(self, world, position, width, height, creation_params: dict = None):
        super().__init__()
        self.world = world  # Reference to the world this entity belongs to
        self.hitbox = Hitbox(position, width, height)  # Initialize hitbox for collision detection

        # Override default width/height if provided in creation_params
        if isinstance(creation_params, dict):
            if creation_params.get("width"):
                self.hitbox.width = int(creation_params["width"])
            if creation_params.get("height"):
                self.hitbox.height = int(creation_params["height"])

    def update(self, delta: float):
        # Method to update the entity each frame; 'delta' is time since last update
        pass

    @property
    def position(self):
        # Getter for entity's position via its hitbox
        return self.hitbox.position

    @position.setter
    def position(self, value):
        # Setter for entity's position via its hitbox
        self.hitbox.position = value

    def onEntityCollision(self, entity):
        # Called when this entity collides with another entity
        pass

    def onBlockCollision(self, block):
        # Called when this entity collides with a block; handle hitbox collision
        self.hitbox.handle_collision(block.hitbox)

    def onBombExplosionCollision(self, bomb):
        # Called when this entity is hit by a bomb explosion; destroy entity
        self.destroy()

    def destroy(self):
        # Remove the entity from the world and stop any sounds it may be playing
        self.stop_sound()
        self.world.remove_entity(self)

    def stop_sound(self):
        # Stop any sound associated with the entity (placeholder)
        pass
