from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", strength_potion())
    print("Testing healing_potion:", healing_potion())


if __name__ == "__main__":
    main()
