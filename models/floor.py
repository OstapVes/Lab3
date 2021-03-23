from models.Repairs import Repairs
from models.materials import Materials


class Floor(Repairs):

    def __init__(self, size: int, material: Materials = Materials):
        self.size = size
        self.Materials = Materials
