def ft_harvest_total():
    i = 1
    x = 0
    while i <= 3:
        x += int(input(f"Day {i} harvest: "))
        i += 1
    print("Total harvest: ", x)
