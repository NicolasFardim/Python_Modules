def count_days(i: int, x: int):
    print("Day ", i)
    if i != x:
        count_days(i+1, x)
    else:
        print("Harvest time!")


def count_harvest_recursive():
    x = int(input("Days until harvest: "))
    if x <= 0:
        print("Harvest time!")
        return
    count_days(1, x)
