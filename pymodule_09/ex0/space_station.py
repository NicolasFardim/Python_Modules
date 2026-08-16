from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def static_test() -> None:
    print("Space Station Data Validation")
    print("=" * 25)
    space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2003, 2, 19, 4, 20, 0),
        is_operational=True,
        notes=None,
    )
    print("Valid station created")
    print(
        f"ID:     {space_station.station_id}\n"
        f"Name:   {space_station.name}\n"
        f"Crew:   {space_station.crew_size}\n"
        f"Power:  {space_station.power_level}\n"
        f"Oxygen: {space_station.oxygen_level}\n"
        f"Status: {'Operational' if space_station.is_operational else 'Off'}\n"
    )
    if space_station.notes:
        print(f"Notes: {space_station.notes}")
    print(f"\n{'=' * 25}")
    print("Expected validation error:")
    try:
        # reminder: pydantic validates all fields first, so if it has a bunch of errors
        # will grab everything and then raise an exception
        wrong_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=2.2,
            oxygen_level=92.3,
            last_maintenance=datetime(2003, 2, 19, 4, 20, 0),
            is_operational=True,
            notes="",
        )
        print(wrong_station)  # it will not print
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")


def main() -> None:
    try:
        from pymodule_09.data_generator import SpaceStationGenerator, DataConfig
    except ImportError:
        print("Data Generator not available, Using static values\n")
        static_test()
        return

    data_config = DataConfig()
    while True:
        try:
            x = int(input("Choose how many Space Station to generate: "))
        except TypeError as e:
            print("ERROR, closing program:", e)
            return
        space_station_gen = SpaceStationGenerator(data_config).generate_station_data(x)

        for station in space_station_gen:
            print("=" * 25)
            try:
                space_station = SpaceStation(**station)
                print("Valid station generated")
                print(
                    f"ID:     {space_station.station_id}\n"
                    f"Name:   {space_station.name}\n"
                    f"Crew:   {space_station.crew_size}\n"
                    f"Power:  {space_station.power_level}\n"
                    f"Oxygen: {space_station.oxygen_level}\n"
                    f"Status: {'Operational' if space_station.is_operational else 'Off'}\n"
                    f"Last maintenance: {space_station.last_maintenance}\n"
                    f"Notes:  {space_station.notes if space_station.notes else 'Empty'}\n"
                )
            except ValidationError as e:
                print("Invalid station generated")
                for error in e.errors():
                    print(f"{error['msg']}")
            print(f"\n{'=' * 25}\n")

        while True:
            check = str(input("\nContinue to generate? [y/n]: "))
            match check.lower():
                case 'y':
                    print("Continuing...\n")
                    break
                case 'n':
                    print("Closing...")
                    return
                case _:
                    print("Invalid input!")
                    continue

        seed = input(f"Change seed (current seed = {data_config.seed})? (enter to not modify)\n")
        if seed == '':
            continue
        try:
            data_config.seed = int(seed)
        except ValueError as e:
            print("Invalid seed! Closing program:", e)
            return


if __name__ == '__main__':
    main()
