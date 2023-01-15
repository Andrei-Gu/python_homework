"""
создайте класс `Plane`, наследник `Vehicle`
"""


from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo: int | float = 0
    max_cargo: int |float


    def __init__(self, weight: int | float, fuel: int | float, fuel_consumption: int | float, max_cargo: int | float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo


    def load_cargo(self, cargo: int | float):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo = self.cargo + cargo
        else:
            raise exceptions.CargoOverload(f'The cargo = {cargo!r} is too heavy. Exceeding max cargo = {self.max_cargo!r}.')


    def remove_all_cargo(self) -> int | float:
        all_cargo = self.cargo
        self.cargo = 0
        return all_cargo
