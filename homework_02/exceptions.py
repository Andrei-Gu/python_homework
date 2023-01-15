"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(ValueError):
    pass


class NotEnoughFuel(ValueError):
    pass


class CargoOverload(ValueError):
    pass