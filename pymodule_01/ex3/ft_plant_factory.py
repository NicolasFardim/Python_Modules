class Plant:
    def __init__(self, name: str, height: float | int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f'Created: {self.name}: {self.height}cm, '
              f'{self.age_days} days old')


def main() -> None:
    plants = [
        Plant('Rose', 45, 5),
        Plant('Oak', 200, 365),
        Plant('Cactus', 5, 90),
        Plant('Sunflower', 80, 45),
        Plant('Fern', 15, 120)
    ]
    for plant in plants:
        plant.show()


if __name__ == '__main__':
    main()
