from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    cadet = "Cadet"
    officer = "Officer"
    lieutenant = "Lieutenant"
    captain = "Captain"
    commander = "Commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    year_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_data: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(
                member.rank in (Rank.commander, Rank.captain)
                for member in self.crew
        ):
            raise ValueError("Must be a commander or captain in the crew")
        for crew_member in self.crew:
            if not crew_member.is_active:
                raise ValueError(f"Crew member '{crew_member.name}' must be active")
        if self.duration_days > 365:
            experienced = sum(1 for member in self.crew if member.year_experience > 5)
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions need 50% experienced crew (5+ years)")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 25)
    crew_member = [
        CrewMember(
            member_id="abc123",
            name="Sarah Connor",
            rank=Rank.commander,
            age=30,
            specialization="Mission Command",
            year_experience=8,
        ),
        CrewMember(
            member_id="dfg456",
            name="John Smith",
            rank=Rank.lieutenant,
            age=37,
            specialization="Navigation",
            year_experience=15,
        ),
        CrewMember(
            member_id="hij789",
            name="Alice Johnson",
            rank=Rank.officer,
            age=26,
            specialization="Engineering",
            year_experience=4,
        ),
    ]

    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        launch_data=datetime(year=2040, month=1, day=1),
        duration_days=5,
        destination="Mars",
        budget_millions=2500.0,
        crew=crew_member,
    )
    print("Valid mission created:")
    print(
        f"Mission: {space_mission.mission_name}\n"
        f"ID: {space_mission.mission_id}\n"
        f"Destination: {space_mission.destination}\n"
        f"Budget: {space_mission.budget_millions}\n"
        f"Crew size: {len(space_mission.crew)}\n"
    )
    print("Crew members:")
    for crew_member in space_mission.crew:
        print(f"- {crew_member.name} ({crew_member.rank.value}) - {crew_member.specialization}")

    print("=" * 25)
    print("Expected validation error:")

    try:
        space_mission2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            launch_data=datetime(year=2040, month=1, day=1),
            duration_days=5,
            destination="Mars",
            budget_millions=2500.0,
            crew=[CrewMember(
                member_id="aaa111",
                name="carlos",
                rank=Rank.officer,
                age=30,
                specialization="Mission Command",
                year_experience=10,
            )],
        )
        print(space_mission2)
    except ValidationError as e:
        for error in e.errors():
            if 'ctx' in error:
                print(error['ctx']['error'])
            else:
                print(error['msg'])


if __name__ == '__main__':
    main()
