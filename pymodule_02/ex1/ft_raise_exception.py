def input_temp(temperature: str) -> int:
    int_temperature: int = int(temperature)
    if int_temperature < 0:
        raise ValueError(f'{int_temperature}°C is too cold for plants'
                         f' (min 0°C)')
    elif int_temperature > 40:
        raise ValueError(f'{int_temperature}°C is too hot for plants'
                         f' (max 40°C)')
    return int_temperature


def test_temperature() -> None:
    print('=== Garden Temperature ===\n')
    temperature: str = '25'
    print(f"input data is '{temperature}'")
    print(f'Temperature is now {input_temp(temperature)}°c\n')

    res: int
    try:
        temperature = 'abc'
        print(f"input data is '{temperature}'")
        res = input_temp('abc')
        print(f'Temperature is now {res}°c')
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print()
    try:
        temperature = '-50'
        print(f"input data is '{temperature}'")
        res = input_temp(temperature)
        print(f'Temperature is now {res}°c')
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print()
    try:
        temperature = '100'
        print(f"input data is '{temperature}'")
        res = input_temp(temperature)
        print(f'Temperature is now {res}°c')
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
