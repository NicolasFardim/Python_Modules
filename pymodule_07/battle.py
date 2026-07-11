from ex0 import CreatureFactory, FlameFactory, AquaFactory


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


def test_battle(fire_factory: FlameFactory, aqua_factory: AquaFactory) -> None:
    print("Testing factory")
    fire_creature = fire_factory.create_base()
    aqua_creature = aqua_factory.create_base()
    print(fire_creature.describe())
    print("vs.")
    print(aqua_creature.describe())
    print("fight!")
    print(fire_creature.attack())
    print(aqua_creature.attack())


def main() -> None:
    fire_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()

    test_factory(fire_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(fire_factory, aqua_factory)


if __name__ == '__main__':
    main()
