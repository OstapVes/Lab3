from models import rosetteetype
from models.electricity import Electricity
from models.Repairs import Repairs
from models.country import Country
from models.category import Category


class Rosette(Electricity):

    def __init__(self, thikness: int = 5, type: rosetteetype = rosetteetype):
        Repairs.__init__(self, 200, "Tytan", Country.Germany, Category.Electricity)
        self.thikness = thikness
        self.type = type