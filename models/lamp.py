from models.electricity import Electricity
from models.Repairs import Repairs
from models.country import Country
from models.category import Category


class Lamp(Electricity):

    def __init__(self, number_of_light_bulbs: int = 15):
        Repairs.__init__(self, 400, "Bryza", Country.Ukraine, Category.Electricity)
        self.number_of_light_bulbs = number_of_light_bulbs
