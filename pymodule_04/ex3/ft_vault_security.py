def secure_archive(filename: str, action: str = 'read', content: str = '') -> tuple[bool, str]:
    try:
        if action == 'read':
            with open(filename, 'r') as file:
                return True, file.read()
        elif action == 'write':
            with open(filename, 'w') as file:
                file.write(content)
                return False, 'Written'
        else:
            raise OSError('Invalid action')
    except OSError as e:
        return False, str(e)


def main() -> None:
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('nao_existent.txt'))
    print()


if __name__ == "__main__":
    main()
