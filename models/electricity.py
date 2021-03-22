from models.Repairs import Repairs


class Electricity(Repairs):

    def __init__(self, brightness: str, number: int):
        self.brightness = brightness
        self.number = number
