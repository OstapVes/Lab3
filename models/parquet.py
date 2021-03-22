from models.floor import Floor
from models.Repairs import Repairs
from models.country import Country
from models.category import Category


class Parquet(Floor):

    def __init__(self, fastening: str = "straight"):
        Repairs.__init__(self, 2000, "Ibud", Country.Ukraine, Category.Floor)
        self.fastening = fastening
