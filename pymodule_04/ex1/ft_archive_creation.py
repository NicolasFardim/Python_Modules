import sys
import typing


def access_data() -> str | None:
    filename: str = sys.argv[1]
    print('=== Cyber Archives Recovery & Preservation ===')
    try:
        print('Accessioning file:', filename)
        file: typing.IO[str] = open(filename, 'r')
    except OSError as e:
        print(f"Error opening file {filename}:", e)
        return None
    content: str = file.read()
    print('---\n')
    print(content)
    print('\n---')
    file.close()
    return content


def transform_data(content) -> None:
    print('Transform data:')
    print('---\n')
    print(content)
    print('\n---')


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_ancient_text.py <file>')
        return

    try:
        content: str | None = access_data()
        if content is None:
            raise OSError
    except OSError:
        return

    new_filename = input('Enter new file name (or empty): ')
    if not new_filename:
        print('Not saving data')
        return
    try:
        print(f"saving data to '{new_filename}'")
        new_file: typing.IO[str] = open(new_filename, 'w')
    except OSError as e:
        print(f"Error opening file {new_filename}:", e)
        return
    new_file.write(content)
    new_file.close()
    print(f"Data saved in file '{new_filename}'")


if __name__ == "__main__":
    main()
