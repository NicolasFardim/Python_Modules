from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_creatures(factory: HealingCreatureFactory):
    sproutling = factory.create_base()
    bloomelle = factory.create_evolved()
    print("Testing Creature with Healing capability")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print(sproutling.heal(bloomelle))
    print(" evolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())
    print(bloomelle.heal(sproutling))


def test_transform_creatures(transform_factory: TransformCreatureFactory):
    shiftling = transform_factory.create_base()
    morphagon = transform_factory.create_evolved()
    print("Testing Creature with Transformation capability")
    print(shiftling.describe())
    print(shiftling.attack())
    shiftling.transform()
    print(shiftling.attack())
    shiftling.revert()
    print(" evolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    morphagon.transform()
    print(morphagon.attack())
    morphagon.revert()


def main():
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_heal_creatures(heal_factory)
    print()
    test_transform_creatures(transform_factory)


if __name__ == '__main__':
    main()
