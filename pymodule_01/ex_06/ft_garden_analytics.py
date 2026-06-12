class Plant:
    def __init__(self, name: str, height: float | int, age: int):
        self._name = name
        self._age = 0
        self._height = 0.0
        self._total_growth = 0.0
        self.set_age(age)
        self.set_height(height)

    def set_age(self, new_age: int):
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print('Age update rejected')
        else:
            self._age = new_age

    def set_height(self, new_height: float | int):
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = round(new_height, 1)

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height

    def grow(self, growth_rate: float | int = 0.8):
        self._height = round(self._height + growth_rate, 1)
        self._total_growth = round(self._total_growth + growth_rate, 1)

    def age_day(self):
        self._age += 1

    def show(self):
        print(f'{self._name}: {self._height:.1f}cm, '
              f'{self._age} days old')


class Flower(Plant):
    def __init__(self, name: str, height: float | int, age: int, color: str):
        self._color = color
        self._bloomed = False
        super().__init__(name, height, age)

    def show(self):
        super().show()
        print(f' Color: {self._color}')
        if self._bloomed:
            print(f' {self._name} is blooming beautifully!')
        else:
            print(f' {self._name} has not bloomed yet')

    def bloom(self):
        if not self._bloomed:
            print('[asking the rose to bloom]')
            self._bloomed = True
        else:
            print('[already blooming]')


class Tree(Plant):
    def __init__(self, name: str, height: float | int, age: int, trunk_diameter: float | int):
        self._trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    def show(self):
        super().show()
        print(f' Trunk diameter: {self._trunk_diameter:.1f}cm')

    def produce_shade(self):
        print(f'[Asking the {self._name} to produce shade]')
        print(f'Tree {self._name} now produces a shade of {self._height:.1f}cm long '
              f'and {self._trunk_diameter:.1f}cm wide')


class Vegetable(Plant):
    def __init__(self, name: str, height: float | int, age: int, harvest_season: str, nutrition_value: int):
        self._nutrition_value = nutrition_value
        self._harvest_season = harvest_season
        super().__init__(name, height, age)

    def show(self):
        super().show()
        print(f' Harvest season: {self._harvest_season}')
        print(f' Nutrition value: {self._nutrition_value}')

    def make_grow(self, days: int):
        for n in range(days):
            super().grow(2.1)
            super().age_day()
            self._nutrition_value += 1
        print(f'[make {self._name} grow and age for 20 days]')


def main():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower('Rose', 1.2, 1, 'red')
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree('Oak', 200, 365, 5)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable('Tomato', 5.0, 10, 'April', 0)
    tomato.show()
    tomato.make_grow(20)
    tomato.show()


if __name__ == '__main__':
    main()
