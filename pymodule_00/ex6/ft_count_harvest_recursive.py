def count_days(day: int, harvest_day: int) -> None:
    print('Day ', day)
    if day != harvest_day:
        count_days(day + 1, harvest_day)
    else:
        print('Harvest time!')


def ft_count_harvest_recursive() -> None:
    harvest_day: int = int(input('Days until harvest: '))
    if harvest_day <= 0:
        print('Harvest time!')
        return
    count_days(1, harvest_day)
