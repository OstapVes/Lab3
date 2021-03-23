from models.Repairs import Repairs


class Walls(Repairs):

    def __init__(self, color: str, materials: str, type_of_surface: str):
        self.color = color
        self.materials = materials
        self.type_of_surface = type_of_surface
