class GardenError(Exception):
    def __init__(self, msg: str = "Unknow plant error") -> None:
        self.args = (msg,)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_tank(liter: int = 20) -> None:
    if liter < 30:
        raise WaterError("Not enough water in the tank!")


def garden_plants(plant: str = 'Tomato', flourishing: bool = False) -> None:
    if not flourishing:
        raise PlantError(f"{plant} is wilting")


def main() -> None:
    print('=== Custom Garden Errors Demo ===')
    print('\nTesting PlantError')
    try:
        water_tank(29)
    except WaterError as e:
        print('Caught:', e)
    print('\nTesting PlantError')
    try:
        garden_plants('Tomato', False)
    except PlantError as e:
        print('Caught:', e)
    print('\nTesting all errors')
    for test in (water_tank, garden_plants):
        try:
            test()
        except GardenError as e:
            print('Caught:', e)
    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    main()
