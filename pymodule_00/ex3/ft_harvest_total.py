def ft_harvest_total() -> None:
    day: int = 1
    total: int = 0
    while day <= 3:
        total += int(input(f'Day {day} harvest: '))
        day += 1
    print('Total harvest: ', total)
