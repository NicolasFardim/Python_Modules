import alchemy.elements


# I could use "import alchemy.elements as elements"
# not sure if subject allows it
def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using: 'import ...' structure\n"
          "Testing create_earth:", alchemy.elements.create_earth())


if __name__ == '__main__':
    main()
