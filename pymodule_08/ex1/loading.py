import importlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests


def check_dependencies():
    pkgs = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "requests": "Network access",
        "matplotlib": "Visualization"
    }

    print("Checking dependencies:")
    try:
        for pkg, task in pkgs.items():
            mod = importlib.import_module(pkg)
            print(f"[OK] {mod.__name__} ({mod.__version__}) - {task} ready")
    except ModuleNotFoundError as e:
        print(e)


def request_data() -> dict[str, str | float]:
    url: str = "https://dummyjson.com/users"
    try:
        response: requests.Response = requests.get(url)
        data: dict[str, str | float] = response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        exit()
    return data


def extract_data(data: dict[str, str | float]) -> tuple[pd.DataFrame, pd.DataFrame]:
    users = data["users"]
    df = pd.DataFrame(users)

    tall_people = df[df["height"] > 180][
        ["firstName", "lastName", "height"]
    ]
    small_people = df[df["height"] < 170][
        ["firstName", "lastName", "height"]
    ]
    return small_people, tall_people


def analyze(small_p: pd.DataFrame, tall_p: pd.DataFrame) -> dict[str, float]:
    analyzed: dict[str, float] = {
        "average_tall": float(np.mean(tall_p["height"])),
        "average_small": float(np.mean(small_p["height"])),
        "smallest": float(np.min(small_p["height"])),
        "tallest": float(np.max(tall_p["height"])),
    }
    return analyzed


def save_img(data: dict[str, float]) -> None:
    plt.title("Avarage size: Small vs Tall", fontweight="bold")

    plt.bar(
        ["Average Small ( < 1.70) ", "Average Tall ( > 1.80)"],
        [data["average_small"], data["average_tall"]],
        color=["red", "green"],
    )
    smallest: int = int(data["smallest"])
    tallest: int = int(data["tallest"])
    plt.ylim(smallest, tallest + 1)
    plt.yticks(range(smallest, tallest + 5, 5))
    plt.ylabel("Height (cm)")
    plt.savefig('average.png')
    plt.close()
    print("Results saved to: average.png")


def main():
    print("LOADING STATUS: Loading programs...")
    check_dependencies()
    data: dict[str, str | float] = request_data()
    small, tall = extract_data(data)
    save_img(analyze(small, tall))


if __name__ == '__main__':
    main()
