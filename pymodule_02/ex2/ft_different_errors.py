def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            num: int = int('abc')
        case 1:
            n1: int = 1
            n2: int = 0
            div = n1 / n2
        case 2:
            open(file='/non/existent/file')
        case 3:
            name: str = 'Nicolas'
            age: int = 19
            name + age
        case _:
            return


def test_error_types():
    print('=== Garden Error Type Demo ===')
    op: int = 0
    while op != 3:
        try:
            print('Testing operation', op)
            garden_operations(op)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print('Caught:', e)
        print('Operation completed successfully')
        op += 1
    print('All error types tested successfully!')


if __name__ == '__main__':
    test_error_types()
