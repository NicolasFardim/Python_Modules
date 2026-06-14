class Plant:
    def __init__(self, name: str, height: float | int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age} days old')


def main() -> None:
    rose = Plant('Rose', 25, 30)
    cactus = Plant('Cactus', 15, 120)
    sunflower = Plant('Sunflower', 80, 45)
    print(f'=== Garden Plant Registry ===')
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == '__main__':
    main()
