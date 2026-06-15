def ft_count_harvest_iterative() -> None:
    harvest_day: int = int(input('Days until harvest: '))
    for day in range(1, harvest_day + 1):
        print('Day ', day)
    print('Harvest time!')
