import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_ancient_text.py <file>')
        return

    filename: str = sys.argv[1]
    print('=== Cyber Archives Recovery ===')
    try:
        print('Accessioning file:', filename)
        file: typing.IO[str] = open(filename, 'r')
    except OSError as e:
        print(f"Error opening file {filename}:", e)
        return

    print('---\n')
    print(file.read())
    print('\n---')
    file.close()
    print(f"File: '{filename}' closed.")


if __name__ == "__main__":
    main()
