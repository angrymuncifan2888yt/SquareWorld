from .block import Block


class StoneBlock(Block):
    def __init__(self, position):
        super().__init__(position, 3)