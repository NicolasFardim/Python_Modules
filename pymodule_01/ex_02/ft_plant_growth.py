class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age_days = age
        self.height = height
        self.total_growth = 0.0

    def grow(self):
        self.height = round(self.height + 0.8, 1)
        self.total_growth = round(self.total_growth + 0.8, 1)

    def age(self):
        self.age_days += 1

    def status(self):
        print(f'{self.name}: {self.height}cm, {self.age_days} days old')


def main():
    rose = Plant('Rose', 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.status()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.status()
    print(f"Growth this week: {rose.total_growth}cm")


if __name__ == '__main__':
    main()
