from alchemy.grimoire import light_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell:",
          light_spell_record("Fantasy", "Earth, Wind and Fire"))


if __name__ == "__main__":
    main()
