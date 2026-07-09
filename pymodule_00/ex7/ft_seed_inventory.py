def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    match unit.lower():
        case 'packets':
            print(f'{seed_type.capitalize()} seeds: '
                  f'{quantity} packets available')
        case 'grams':
            print(f'{seed_type.capitalize()} seeds: '
                  f'{quantity} grams total')
        case 'area':
            print(f'{seed_type.capitalize()} seeds: covers '
                  f'{quantity} square meters')
        case _:
            print('Unknown unit type')
