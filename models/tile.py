from models.floor import Floor
from models.Repairs import Repairs
from models.country import Country
from models.category import Category


class Tile(Floor):

    def __init__(self, strength: str = "Sturdy", distance: int = 5):
        Repairs.__init__(self, 1200, "Tytan", Country.Ukraine, Category.Floor)
        self.strength = strength
        self.distance = distance
