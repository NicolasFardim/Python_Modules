import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file>')
        return

    filename: str = sys.argv[1]
    print('=== Cyber Archives Recovery ===')
    try:
        print(f"Accessing file: '{filename}'")
        file: typing.IO[str] = open(filename, 'r')
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print('---\n')
    print(file.read())
    print('\n---')
    file.close()
    print(f"File: '{filename}' closed.")


if __name__ == "__main__":
    main()
