import sys


def parse_args() -> dict[str, int]:
    bag: dict[str, int] = {}
    for item in sys.argv[1:]:
        if ':' not in item:
            print(f"Error - Invalid parameter '{item}'")
            continue
        try:
            key, value = item.split(':')
            if not key:
                raise ValueError(f"Error - Empty key '{item}'")
        except ValueError as e:
            print(e)
            continue
        if key in bag:
            print(f"Redundant item '{key}' - discarding ")
        else:
            try:
                quantity = int(value)
                if quantity <= 0:
                    raise ValueError(f"can't accept 0 or less: {quantity}")
                bag[key] = quantity
            except ValueError as e:
                print(f"Quantity error for '{key}': {e}")
                continue
    return bag


def ft_max(bag: dict[str, int]) -> str:
    max_i: int = 0
    item: str
    for key in bag:
        if bag[key] > max_i:
            max_i = bag[key]
            item = key
    return item


def ft_min(bag: dict[str, int]) -> str:
    min_i: int = 0
    item: str
    for key in bag:
        if min_i == 0:
            min_i = bag[key]
            item = key
        if bag[key] < min_i:
            min_i = bag[key]
            item = key
    return item


def main() -> None:
    bag: dict[str, int] = parse_args()
    if bag:
        print('Got inventory:', bag)
        print('Item list:', list(bag.keys()))
        print(f'Total quantity of {len(bag.keys())} '
              f'items: {sum(bag.values())}')
        for key in bag:
            percentage = round(bag[key] / sum(bag.values()) * 100, 1)
            print(f"Item {key} represents {percentage}%")
        print(f'Item most abundant: {ft_max(bag)} with {bag[ft_max(bag)]}')
        print(f'Item least abundant: {ft_min(bag)} with {bag[ft_min(bag)]}')
    else:
        print('Bag is empty')
    bag.update({'Magic item': 1})
    print(f'Bag is updated: {bag}')


if '__main__' == __name__:
    main()
