class Plant:
    def __init__(self, name: str, height: float | int, age: int) -> None:
        self.name = name
        self.age_days = age
        self.height = height
        self.total_growth = 0.0

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)
        self.total_growth = round(self.total_growth + 0.8, 1)

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f'{self.name}: {self.height:.1f}cm, {self.age_days} days old')


def main() -> None:
    rose = Plant('Rose', 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {rose.total_growth:.1f}cm")


if __name__ == '__main__':
    main()
