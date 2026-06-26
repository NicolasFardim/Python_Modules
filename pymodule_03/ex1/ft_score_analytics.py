import sys


def main() -> None:
    print('=== Player Score Analytics ===')
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f'Invalid parameter: {arg}')
    if len(scores) > 0:
        print(f'Scores processed: {scores}')
        print(f'Total players: {len(scores)}')
        print(f'Total score: {sum(scores)}')
        print(f'Average score: {sum(scores) / len(scores):.1f}')
        print(f'Highest score: {max(scores)}')
        print(f'Low score: {min(scores)}')
        print(f'Score range: {max(scores) - min(scores)}')
    else:
        print('No scores provided. Usage: ', *sys.argv)


if __name__ == '__main__':
    main()
