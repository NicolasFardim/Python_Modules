def input_temp(temperature: str) -> int:
    return int(temperature)


def test_temperature() -> None:
    print('=== Garden Temperature ===\n')
    temperature: str = '25'
    print(f"input data is '{temperature}'")
    print(f'Temperature is now {input_temp(temperature)}°c\n')
    try:
        temperature = 'abc'
        print(f"input data is '{temperature}'")
        res: int = input_temp(temperature)
        print(f'Temperature is now {res}°c')
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
