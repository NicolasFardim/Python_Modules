import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'\n"
          "Testing create_air:", alchemy.create_air())
    print("Now show that not all functions can be reached\n"
          "This will raise an exception!")

    print(f"Testing the hidden create_earth: "
          f"{alchemy.create_earth()}")  # type: ignore[attr-defined]


if __name__ == '__main__':
    main()
