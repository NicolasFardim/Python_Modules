def secure_archive(
        filename: str, action: str = 'read', content: str = '') \
        -> tuple[bool, str]:
    try:
        if action == 'read':
            with open(filename, 'r') as file:
                return True, file.read()
        elif action == 'write':
            with open(filename, 'w') as file:
                file.write(content)
                return True, "Content successfully written to a file"
        else:
            raise OSError('Invalid action')
    except OSError as e:
        return False, str(e)


def main() -> None:
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('nao_existent.txt'))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/blocked/master.passwd', 'read'))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt', 'read'))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive('ancient_fragment.txt', 'write', content='teste'))


if __name__ == "__main__":
    main()
