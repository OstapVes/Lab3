from models.country import Country
from models.category import Category


class Repairs:

    def __init__(self, price: float, brand: str, origin_country: Country = Country, category: Category = Category):
        self.price = price
        self.brand = brand
        self.origin_country = origin_country
        self.Category = Category

    def __str__(self):
        return f" Price: {self.price}\n Brand: {self.brand}\n "
