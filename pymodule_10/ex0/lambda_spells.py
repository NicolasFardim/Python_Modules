def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: spell.replace(' ', ''), spells))


def mage_stats(mages: list[dict]) -> dict:
    pass


def test_sorter(artifacts: list[dict]) -> None:
    print("Testing artifact sorter...")
    print("Normal Artifacts order: ")
    for art in artifacts:
        print(f"{art['name']} ({art['power']} power - {art['type']} type)")

    print("\nSorted:")
    reversed_artifacts = artifact_sorter(artifacts)
    for i, art in enumerate(reversed_artifacts):
        print(f"{art['name']} ({art['power']} power - {art['type']} type)", end="")
        if i + 1 < len(reversed_artifacts):
            print(f" comes before {reversed_artifacts[i + 1]['name']}"
                  f" ({reversed_artifacts[i + 1]['power']} power)")
        else:
            print(" weakest artifact\n")


def main() -> None:
    try:
        from pymodule_10.data_generator import FuncMageDataGenerator
        func_mage_data = FuncMageDataGenerator()
        artifacts = func_mage_data.generate_artifacts()
        mages = func_mage_data.generate_mages()
        spells = func_mage_data.generate_spells()
    except ImportError:
        func_mage_data = None
        print("Not using FuncMage to generate Data!\n")
        artifacts = [
            {'name': 'Earth Shield', 'power': 82, 'type': 'weapon'},
            {'name': 'Water Chalice', 'power': 98, 'type': 'focus'},
            {'name': 'Shadow Blade', 'power': 102, 'type': 'focus'},
            {'name': 'Lightning Rod', 'power': 68, 'type': 'weapon'}
        ]
        mages = [
            {'name': 'Zara', 'power': 87, 'element': 'earth'},
            {'name': 'Kai', 'power': 77, 'element': 'water'},
            {'name': 'Jordan', 'power': 51, 'element': 'light'},
            {'name': 'Rowan', 'power': 87, 'element': 'fire'},
            {'name': 'Casey', 'power': 81, 'element': 'lightning'}
        ]
        spells = ['meteor', 'heal', 'flash', 'darkness']

    test_sorter(artifacts)


if __name__ == "__main__":
    main()
