from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print("Testing record dark spell:",
          dark_spell_record(
              "Dark", "Bat, Bog and Arsenic"
          ))


if __name__ == "__main__":
    main()
