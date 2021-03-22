from models.electricity import Electricity
from models.Repairs import Repairs
from models.country import Country
from models.category import Category


class Conducts(Electricity):

    def __init__(self, materials: str = "Copper"):
        Repairs.__init__(self, 1500, "Struga", Country.USA, Category.Electricity)
        self.materials = materials
