from project.medicine.medicine import Medicine
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: list = []
        self.supplies: list = []
        self.medicine: list = []

    @property
    def food(self):
        food_data = [supply for supply in self.supplies if supply.__class__.__name__ == 'FoodSupply']
        if not food_data:
            raise IndexError('There are no food supplies left!')
        return food_data

    @property
    def water(self):
        water_data = [supply for supply in self.supplies if supply.__class__.__name__ == 'WaterSupply']
        if not water_data:
            raise IndexError('There are no water supplies left!')
        return water_data

    @property
    def painkillers(self):
        painkillers_data = [medicine for medicine in self.medicine if medicine.__class__.__name__ == 'Painkiller']
        if not painkillers_data:
            raise IndexError('There are no painkillers left!')
        return painkillers_data

    @property
    def salves(self):
        salves_data = [medicine for medicine in self.medicine if medicine.__class__.__name__ == 'Salve']
        if not salves_data:
            raise IndexError('There are no painkillers left!')
        return salves_data

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            for medicine in self.medicine[::-1]:
                if medicine.__class__.__name__ == medicine_type:
                    medicine.apply(survivor)
                    self.medicine.remove(medicine)
                    # self.__remove_medicine_by_type(medicine_type)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for supply in self.supplies[::-1]:
                if supply.__class__.__name__ == sustenance_type:
                    supply.apply(survivor)
                    self.supplies.remove(supply)
                    # self.__remove_supply_by_type(sustenance_type)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            FoodSupply().apply(survivor)
            WaterSupply().apply(survivor)

    # If remove of property data needed
    # def __remove_medicine_by_type(self, medicine_type):
    #     if medicine_type == 'Painkiller':
    #         self.painkillers.pop()
    #     else:
    #         self.salves.pop()
    #
    # def __remove_supply_by_type(self, sustenance_type):
    #     if sustenance_type == 'FoodSupply':
    #         self.food.pop()
    #     else:
    #         self.water.pop()
