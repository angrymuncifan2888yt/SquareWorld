# Adds health system to an entity
class HasHealth:
    def __init__(self):
        # Maximum health value
        self.max_hp = None

        # Current health value
        self.hp = None

        # Death state flag
        self.is_dead = False

    def damage(self, amount: int):
        # Apply damage to the entity
        if self.is_dead:
            return

        self.hp -= amount

        # Check for death
        if self.hp <= 0:
            self.hp = 0
            self.is_dead = True
            self.on_death()

    def heal(self, amount: int):
        # Heal entity up to max HP
        if self.is_dead:
            return

        self.hp = min(self.max_hp, self.hp + amount)

    def kill(self):
        # Instantly kill the entity
        if self.is_dead:
            return

        self.hp = 0
        self.is_dead = True
        self.on_death()

    def revive(self):
        # Fully restore HP and revive entity
        self.hp = self.max_hp
        self.is_dead = False

    def set_max_hp(self, value: int):
        # Set a new maximum HP value
        self.max_hp = value
        self.hp = min(self.hp, self.max_hp)

    def on_death(self):
        """
        Called when HP reaches zero.
        Override this method in the entity class.
        """
        pass
