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


def main() -> None:
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


if __name__ == '__main__':
    main()
