import random


def main():
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']

    capitalized_names = [name.capitalize() for name in players]
    capitalized_only = [name for name in players if name.istitle()]

    scores = {name: random.randint(0, 1000) for name in capitalized_names}
    average = sum(scores.values()) / len(scores)
    high_scores = {name: score for name, score in scores.items() if score > average}

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {capitalized_only}")
    print(f"Score dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == '__main__':
    main()
