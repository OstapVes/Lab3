from models.tile import Tile
from models.parquet import Parquet
from models.rosette import Rosette
from models.conducts import Conducts
from models.linoleum import Linoleum
from models.lamp import Lamp
from manager.repairs_manager import RepairsManager
from manager.sort_order import SortOrder


class Test:

    def __init__(self):
        pass

    def main(self):
        manager = RepairsManager([Parquet(), Tile(), Linoleum(), Conducts(), Rosette(), Lamp()])
        print("\n\n=================\nItems for repair:\n=================\n\n\n ")
        manager.print_repairs()
        print("\n\n\n========================\nSorted by price min-max:\n========================\n\n\n")
        manager.sort_by_price(SortOrder.ASC)
        manager.print_repairs()
        print("\n\n\n========================\nSorted by price max-min:\n========================\n\n\n")
        manager.sort_by_price(SortOrder.DESC)
        manager.print_repairs()
        print("\n\n\n====================\nSorted by brand A-Z:\n====================\n\n\n")
        manager.sort_by_brand(SortOrder.ASC)
        manager.print_repairs()
        print("\n\n\n====================\nSorted by brand Z-A:\n====================\n\n\n")
        manager.sort_by_brand(SortOrder.DESC)
        manager.print_repairs()
