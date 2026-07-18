import importlib


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


def main():
    print("LOADING STATUS: Loading programs...")
    check_dependencies()


if __name__ == '__main__':
    main()
