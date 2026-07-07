from .dark_validator import validate_dark_ingredient


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return (f"Spell recorded: "
            f"{spell_name} {validate_dark_ingredient(ingredients)})")
