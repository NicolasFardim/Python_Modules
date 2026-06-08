def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    unit = unit.lower()
    match unit:
        case "packets":
            print(f"{seed_type} seeds: {quantity} packets available")
        case "grams":
            print(f"{seed_type} seeds: {quantity} grams total")
        case "area":
            print(f"{seed_type} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")
