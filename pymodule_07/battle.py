from ex0 import CreatureFactory, FlameFactory


def test_factory(creature_factory: CreatureFactory) -> None:
    print("Testing Factory")

    creature_base = creature_factory.create_base()
    if creature_base:
        print(creature_base.describe())
        print(creature_base.attack())

    creature_evolved = creature_factory.create_evolved()
    if creature_evolved:
        print(creature_evolved.describe())
        print(creature_evolved.attack())


def main():
    fire_factory = FlameFactory()

    test_factory(fire_factory)


if __name__ == '__main__':
    main()
