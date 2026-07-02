import random
import typing

players: list[str] = ['dylan', 'alice', 'bob', 'charlie']
actions: list[str] = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(players), random.choice(actions)


def consume_events(events: list[tuple[str, str]]) \
        -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index: int = random.randint(0, len(events) - 1)
        item: tuple[str, str] = events[index]
        events[:] = events[:index] + events[index + 1:]
        yield item


def main() -> None:
    generator: typing.Generator[tuple[str, str], None, None] = gen_event()
    for i in range(0, 10):
        event: tuple[str, str] = next(generator)
        print(f'Event {i}: Player {event[0]} did action {event[1]}')

    events: list[tuple[str, str]] = []
    for i in range(0, 10):
        events += [next(generator)]
    print('Built list of 10 events:', events)
    for event in consume_events(events):
        print('Got event:', event)
        print('Remaining in list:', events)


if __name__ == '__main__':
    main()
