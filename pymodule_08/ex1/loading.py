import importlib

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


def request_data() -> requests.Response:
    url = "https://dummyjson.com/users"
    response: requests.Response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed to fetch data")
        exit()
    return data


def extract_data(data: requests.Response) -> tuple[pd.DataFrame, pd.DataFrame]:
    users = data["users"]
    df = pd.DataFrame(users)

    tall_people = df[df["height"] > 180][
        ["firstName", "lastName", "height"]
    ]
    small_people = df[df["height"] < 170][
        ["firstName", "lastName", "height"]
    ]
    return small_people, tall_people


def analyze(small_people: pd.DataFrame, tall_people: pd.DataFrame) -> tuple[np.float64, np.float64]:
    average_small = np.mean(small_people["height"])
    average_tall = np.mean(tall_people["height"])
    return average_small, average_tall


def main():
    print("LOADING STATUS: Loading programs...")
    data: requests.Response = request_data()
    small, tall = extract_data(data)
    analyze(small, tall)


if __name__ == '__main__':
    main()
