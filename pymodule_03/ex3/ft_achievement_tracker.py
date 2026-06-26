import random

achievements: tuple[str, ...] = (  # noqa
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer'
)


def gen_player_achievements() -> set:
    n: int = int(
        random.triangular(0, len(achievements) + 1, len(achievements) / 2)
    )
    return set(random.sample(achievements, n))


def main():
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dan = gen_player_achievements()

    print('=== Achievement Tracker System ===\n')
    # print all players achievements
    print('Alice:', alice)
    print('Bob:', bob)
    print('Charlie:', charlie)
    print('Dan:', dan)
    print()
    print('All distinct achievements:', set.union(alice, bob, charlie, dan))

    # print the common achievements  that all players share
    print('Common achievements:', set.intersection(alice, bob, charlie, dan))
    print()

    # print each player own achievements
    print('Only Alice has:', alice.difference(bob, charlie, dan))
    print('Only Bob has:', bob.difference(alice, charlie, dan))
    print('Only Charlie has:', charlie.difference(alice, bob, dan))
    print('Only Dan has:', dan.difference(alice, bob, charlie))
    print()

    # print each player missing achievement
    print('Alice is missing:', set(achievements).difference(alice))
    print('Bob is missing:', set(achievements).difference(bob))
    print('Charlie is missing:', set(achievements).difference(charlie))
    print('Dan is missing:', set(achievements).difference(dan))


if __name__ == '__main__':
    main()
