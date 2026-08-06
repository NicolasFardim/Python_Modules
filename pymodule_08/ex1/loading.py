import importlib

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     import pandas as pd
#     import numpy as np
#     import matplotlib.pyplot as plt
#     import requests


np = None
pd = None
plt = None
requests = None


def check_dependencies() -> bool:
    global pd, np, plt, requests
    pkgs: dict[str, tuple[str, str]] = {
        "pandas": ("Data manipulation", "3.0.5"),
        "numpy": ("Numerical computation", "2.5.1"),
        "requests": ("Network access", "2.34.2"),
        "matplotlib": ("Visualization", "3.11.1")
    }
    missing = []
    mods = []
    print("Checking dependencies:")
    for pkg, task in pkgs.items():
        try:
            mods.append((importlib.import_module(pkg), task[1]))
            print(f"[OK] {mods[-1][0].__name__} ({mods[-1][0].__version__})"
                  f" - {task[0]} ready")
        except ModuleNotFoundError:
            missing.append(pkg)
            print(f"[KO] missing {pkg}")
    if missing:
        print(f"\nMissing: {missing}"
              f"\nInstall using pip: pip install -r requirements.txt")
        return False
    print()
    for mod in mods:
        if mod[0].__version__ != mod[1]:
            print(f"Warning: package '{mod[0].__name__}' installed version: "
                  f"{mod[0].__version__} Recommended version: {mod[1]}")
        if mod[0].__name__ == "pandas":
            pd = mod[0]
        if mod[0].__name__ == "numpy":
            np = mod[0]
        if mod[0].__name__ == "matplotlib":
            plt = importlib.import_module("matplotlib.pyplot")
        if mod[0].__name__ == "requests":
            requests = mod[0]
    return True


def request_data() -> dict[str, str | float]:
    url: str = "https://dummyjson.com/users"
    try:
        response = requests.get(url)
        data: dict[str, str | float] = response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        exit()
    return data


def analyze(data: dict[str, str | float]) -> dict[str, float]:
    users = data["users"]
    df = pd.DataFrame(users)

    tall_p = df[df["height"] > 180][
        ["firstName", "lastName", "height"]
    ]
    small_p = df[df["height"] < 170][
        ["firstName", "lastName", "height"]
    ]

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
    try:
        plt.savefig('average.png')
        print("Results saved to: average.png")
    except OSError as e:
        print("Error:", e)
    finally:
        plt.close()


def show_versions() -> None:
    print("\nInstalled package versions:")
    pkgs = ["pandas", "numpy", "matplotlib", "requests"]
    for pkg in pkgs:
        try:
            mod = importlib.import_module(pkg)
            print(f"  {pkg}: {mod.__version__}")
        except ModuleNotFoundError:
            print(f"  {pkg}: not installed")


def manual() -> None:
    print("Using pip:")
    print("Setup venv (recommended): $ python3 -m venv <venv_name>\n"
          "Activate venv (linux): $ source <venv>/bin/activate\n"
          "Get the required packages pip install -r requirements.txt\n"
          "Run loading.py: python3 loading.py")

    print("Using poetry")
    print("poetry run python3 loading.py")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    if check_dependencies():
        data: dict[str, str | float] = request_data()
        save_img(analyze(data))
    show_versions()
    print()
    manual()


if __name__ == '__main__':
    main()
