class Plant:
    def __init__(self, name: str, height: float | int, age: int) -> None:
        self._name = name
        self._age = 0
        self._height = 0.0
        self._total_growth = 0.0
        self.set_age(age)
        self.set_height(height)
        self._stats = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self._calls = {'grow': 0, 'age': 0, 'show': 0}

        def display_stats(self) -> None:
            print(f'Stats: {self._calls['grow']} grow, {self._calls['age']} age, {self._calls['show']} show')

        def increment(self, call_type: str) -> None:
            self._calls[call_type] += 1

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print('Age update rejected')
        else:
            self._age = new_age

    def set_height(self, new_height: float | int) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = round(new_height, 1)

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float | int:
        return self._height

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> 'Stats':
        return self._stats

    def grow(self, growth_rate: float | int = 0.8) -> None:
        self._height = round(self._height + growth_rate, 1)
        self._total_growth = round(self._total_growth + growth_rate, 1)
        self._stats.increment('grow')

    def age_day(self) -> None:
        self._age += 1
        self._stats.increment('age')

    def show(self) -> None:
        print(f'{self._name}: {self._height:.1f}cm, '
              f'{self._age} days old')
        self._stats.increment('show')

    @classmethod
    def anon(cls) -> 'Plant':
        return cls("Anonymous", 0, 0)

    @staticmethod
    def check_year_old(age: int) -> bool:
        return age > 365


class Flower(Plant):
    def __init__(self, name: str, height: float | int, age: int, color: str) -> None:
        self._color = color
        self._bloomed = False
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print(f' Color: {self._color}')
        if self._bloomed:
            print(f' {self._name} is blooming beautifully!')
        else:
            print(f' {self._name} has not bloomed yet')

    def bloom(self) -> None:
        if not self._bloomed:
            print(f'[asking the {self._name} to grow and bloom]')
            self.grow()
            self._bloomed = True
        else:
            print('[already blooming]')


class Seed(Flower):
    def __init__(self, name: str, height: float | int, age: int, color: str) -> None:
        self._seed_quantity = 0
        super().__init__(name, height, age, color)

    def show(self) -> None:
        super().show()
        print(f' Seeds: {self._seed_quantity}')

    def make_grow(self, days: int) -> None:
        for n in range(days):
            self.grow(1.5)
            self.age_day()
            self._seed_quantity += 2
        if not self._bloomed:
            self._bloomed = True
        print(f'[make {self._name} grow, age and bloom]')


class Tree(Plant):
    def __init__(self, name: str, height: float | int, age: int, trunk_diameter: float | int) -> None:
        self._trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._calls['shade'] = 0

        def display_stats(self) -> None:
            super().display_stats()
            print(f' {self._calls['shade']} shade')

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {self._trunk_diameter:.1f}cm')

    def produce_shade(self) -> None:
        self._stats.increment('shade')
        print(f'[Asking {self._name} to produce shade]')
        print(f'Tree {self._name} now produces a shade of {self._height:.1f}cm long '
              f'and {self._trunk_diameter:.1f}cm wide')


def display(plant: 'Plant') -> None:
    print(f'[Statistics for {plant.get_name()}]')
    plant.get_stats().display_stats()


def main() -> None:
    rose = Flower('Rose', 15.0, 10, 'Red')
    sunflower = Seed('Sunflower', 80.0, 45, 'Yellow')
    oak = Tree('Oak', 200, 365, 5)
    cupuasu = Plant.anon()

    print('=== Garden statistics ===')
    print('== Check year-old')
    print('Is 30 days more than a year? ->', Plant.check_year_old(30))
    print('Is 400 days more than a year? ->', Plant.check_year_old(400))
    print('\n=== Flower')
    rose.show()
    display(rose)
    print('\n=== Tree')
    oak.show()
    display(oak)
    oak.produce_shade()
    oak.show()
    display(oak)
    print('\n=== Seeds')
    sunflower.show()
    sunflower.make_grow(20)
    sunflower.show()
    display(sunflower)
    print('\n=== Anonymous')
    cupuasu.show()
    display(cupuasu)


if __name__ == '__main__':
    main()
