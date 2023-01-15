from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight: int = 1500
    started: bool = False
    fuel: int = 100
    fuel_consumption: int = 10


    def __init__(self, weight: int | float, fuel: int | float, fuel_consumption: int | float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('Low fuel. Add some fuel.')


#     1st variant of method "move".
#     It's logic correct, because you can't move if the engine isn't started yet.
#     And you can't start the engine if there's no fuel (fuel = 0).
#     And the engine stops (started = True  ->   started = False) when the fuel is over (fuel = 5  ->  fuel = 0).
#     This variant raises LowFuelError if fuel = 0.
#     But "test_move_low_fuel[move_when_zero_fuel]" expects "NotEnoughFuel" error if fuel = 0. IMHO, it's incorrect.
#
#     def move(self, distance: int | float) -> None:
#         if not self.started:
#             self.start()
#         need_for_fuel = distance * self.fuel_consumption
#         if self.fuel >= need_for_fuel:
#             self.fuel = self.fuel - need_for_fuel
#         else:
#             raise exceptions.NotEnoughFuel(f'Not enough fuel to cover the distance = {distance!r}.')


#     2nd variant of method "move" to pass tests
    def move(self, distance: int | float) -> None:
        need_for_fuel = distance * self.fuel_consumption
        if self.fuel == 0 or self.fuel < need_for_fuel:
            raise exceptions.NotEnoughFuel(f'Not enough fuel to cover the distance = {distance!r}.')
        else:
            self.fuel = self.fuel - need_for_fuel
