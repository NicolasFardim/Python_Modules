import sys
import typing


def print_content(content: str) -> None:
    print('---\n')
    print(content)
    print('\n---')


def access_data() -> str | None:
    filename: str = sys.argv[1]
    try:
        print('Accessing file:', sys.argv[1])
        file: typing.IO[str] = open(filename, 'r')
    except OSError as e:
        sys.stderr.write(f'[STDERR] Error opening file {filename}: {e}\n')
        return None
    content: str = file.read()
    file.close()
    return content


def transform_data(content: str) -> str:
    content_lines: list[str] = content.splitlines()
    transformed: list[str] = [line + '#' for line in content_lines]
    return '\n'.join(transformed)


def save_data(content: str) -> None:
    sys.stdout.write('Enter new file name (or empty): ')
    sys.stdout.flush()
    new_filename = sys.stdin.readline().rstrip('\n')

    if not new_filename:
        print('Not saving data')
        return
    try:
        print(f"saving data to '{new_filename}'")
        new_file: typing.IO[str] = open(new_filename, 'w')
    except OSError as e:
        sys.stderr.write(f"[STDERR] '{new_filename}': {e}\n")
        return
    new_file.write(content)
    new_file.close()


def main() -> None:
    if len(sys.argv) != 2:
        sys.stderr.write(f'[STDERR] Usage: {sys.argv[0]} <file>\n')
        return

    print('=== Cyber Archives Recovery & Preservation ===')
    # access and just read
    content: str | None = access_data()
    if content is None:
        return
    print(f"File '{sys.argv[1]}' closed")
    print_content(content)

    # receive content and insert # in the end of each line
    transformed: str = transform_data(content)
    print_content(transformed)

    # if an input is received, creates a new file (with the input name)
    # and write the transformed content in it
    save_data(transformed)


if __name__ == "__main__":
    main()
