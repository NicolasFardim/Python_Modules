from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except Exception as e:
                print("Battle error, aborting tournament: ", e)
                return


def names(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    name_list: list[str] = []
    for factory, strategy in opponents:
        name_list.append(f"({factory.get_name()}+{strategy.get_name()})")
    print(name_list)


def main() -> None:
    normal_strategy: BattleStrategy = NormalStrategy()
    aggressive_strategy: BattleStrategy = AggressiveStrategy()
    defensive_strategy: BattleStrategy = DefensiveStrategy()

    flame_factory: CreatureFactory = FlameFactory()
    healing_factory: CreatureFactory = HealingCreatureFactory()
    aqua_factory: CreatureFactory = AquaFactory()
    transform_factory: CreatureFactory = TransformCreatureFactory()

    tournament1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy)
    ]

    tournament2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy)
    ]

    tournament3: list[tuple[CreatureFactory, BattleStrategy]] = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy)
    ]

    print("Tournament 1 (basic)")
    names(tournament1)
    battle(tournament1)

    print("\nTournament 2 (error)")
    names(tournament2)
    battle(tournament2)

    print("\nTournament 3 (multiple)")
    names(tournament3)
    battle(tournament3)


if __name__ == '__main__':
    main()
