import math


def get_player_pos() -> tuple[float, float, float]:
    x: float = 0
    y: float = 0
    z: float = 0
    while True:
        try:
            str_x: str
            str_y: str
            str_z: str
            str_x, str_y, str_z = input("Enter new coordinates as floats in "
                                        "format 'x,y,z': ").split(',')
        except ValueError:
            print('Invalid syntax')
            continue
        try:
            for bad_coord in (str_x, str_y, str_z):
                float(bad_coord.strip())
            x, y, z = (
                round(float(str_x), 1),
                round(float(str_y), 1),
                round(float(str_z), 1)
            )
            break
        except ValueError as e:
            print(f'Error on parameter "{bad_coord.strip()}": {e}')  # noqa
    return x, y, z


def distance_points(set_one: tuple[float, float, float],
                    set_two: tuple[float, float, float]) -> float:
    distance = math.sqrt((set_two[0] - set_one[0]) ** 2
                         + (set_two[1] - set_one[1]) ** 2
                         + (set_two[2] - set_one[2]) ** 2)
    return distance


def main() -> None:
    print('=== Game Coordinate System ===\n')
    print('Get a first set of coordinates')
    coords1: tuple[float, float, float] = get_player_pos()
    print(f'Got a first tuple: {coords1}\nIt includes: '
          f'X={coords1[0]}, Y={coords1[1]}, Z={coords1[2]}')
    print(f'Distance to the center: {distance_points(coords1, (0, 0, 0)):.4f}')
    print('\nGet a second set of coordinates')
    coords2: tuple[float, float, float] = get_player_pos()
    print(f'Got a second tuple: {coords2}')
    print(f'Distance between the 2 sets of coordinates: '
          f'{distance_points(coords1, coords2):.4f}')


if __name__ == '__main__':
    main()
