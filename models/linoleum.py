from models.floor import Floor
from models.Repairs import Repairs
from models.country import Country
from models.category import Category


class Linoleum(Floor):

    def __init__(self, thikness: int = 0):
        Repairs.__init__(self, 800, "Plastmo", Country.Ukraine, Category.Floor)
        self.thikness = thikness
