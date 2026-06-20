#!/usr/bin/env python3

def main() -> None:
    print('=== Welcome to My Garden ===')
    name: str = 'Rose'
    height: float | int = 25
    age: int = 30
    print(f'Plant: {name}')
    print(f'Height: {height:.1f}cm')
    print(f'Age: {age} days')
    print('\n=== End of Program ===')


if __name__ == '__main__':
    main()
