def validate_ingredient(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    for allowed in light_spell_allowed_ingredients():
        if allowed.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
