class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._age = 0
        self._height = 0.0
        self._total_growth = 0.0
        self.set_age(age, silent=True)
        self.set_height(height, silent=True)
        print('Plant created: ', end='')
        self.show()

    def set_age(self, new_age, silent=False):
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print('Age update rejected')
        else:
            self._age = new_age
            if not silent:
                print(f'Age updated: {self._age} days')

    def set_height(self, new_height, silent=False):
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = round(new_height, 1)
            if not silent:
                print(f'Height updated: {self._height:.1f}cm')

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height

    def grow(self):
        self._height = round(self._height + 0.8, 1)
        self._total_growth = round(self._total_growth + 0.8, 1)

    def age_days(self):
        self._age += 1

    def show(self):
        print(f'{self._name}: {self._height:.1f}cm, '
              f'{self._age} days old')


def main():
    print('=== Garden Security System ===')
    rose = Plant('Rose', 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print()
    print('Current: ', end='')
    rose.show()


if __name__ == '__main__':
    main()
