class GardenError(Exception):
    def __init__(self, msg: str = 'Unknow plant error') -> None:
        self.args = msg,


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plan(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f'Watering {plant_name}: [OK]')


def test_watering_system(plants: list) -> None:
    print('Opening watering system')
    try:
        for plant in plants:
            water_plan(plant)
    except GardenError as e:
        print('Caught PlantError: ', e)
        print('.. ending tests and returning to main')
        return
    finally:
        print('closing watering system')


def main() -> None:
    print('Testing valid plants...')
    test_watering_system(['Tomato', 'Lettuce', 'Carrots'])
    print('\nTesting invalid plants...')
    test_watering_system(['Tomato', 'lettuce', 'Carrots'])


if __name__ == '__main__':
    main()
