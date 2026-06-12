class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    rose = Plant('Rose', 25, 30)
    print(rose)


if __name__ == '__main__':
    main()
