from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        if (self.contact_type is ContactType.physical
                and not self.is_verified):
            raise ValueError("Physical contact must be verified")
        if (self.contact_type is ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact must be at least 3")
        if (self.signal_strength > 7.0
                and not self.message_received):
            raise ValueError(
                "Signal strength greater than 7.0 "
                "should include a received message"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 25)
    alien_contact: AlienContact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(year=2024, month=1, day=1),
        contact_type=ContactType.radio,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )

    print(
        f"Valid contact report:\n"
        f"ID: {alien_contact.contact_id}\n"
        f"Type: {alien_contact.contact_type.value}\n"
        f"Location: {alien_contact.location}\n"
        f"Signal: {alien_contact.signal_strength}/10\n"
        f"Duration: {alien_contact.duration_minutes} minutes\n"
        f"Witnesses: {alien_contact.witness_count}"
    )
    if alien_contact.message_received:
        print(f"Message: {alien_contact.message_received}")
    print(f"\n{'=' * 25}")

    try:
        invalid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(year=2024, month=1, day=1),
            contact_type=ContactType.radio,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received=None
        )
        print(invalid_contact)
    except ValidationError as e:
        for error in e.errors():
            if 'ctx' in error:
                print(error['ctx']['error'])
            else:
                print(error['msg'])


if __name__ == '__main__':
    main()
