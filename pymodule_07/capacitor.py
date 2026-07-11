from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_creatures(factory: HealingCreatureFactory):
    sproutling = factory.create_base()
    heal_creature_evolved = factory.create_evolved()
    print("Testing Creature with Healing capability")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())


def test_transform_creatures(transform_factory: TransformCreatureFactory):
    pass


def main():
    heal_factory = HealingCreatureFactory()
    test_heal_creatures(heal_factory)


if __name__ == '__main__':
    main()
