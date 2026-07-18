import os
import site
import sys


def main() -> None:
    inside_venv: bool = sys.prefix != sys.base_prefix

    print("MATRIX STATUS:", end=' ')
    if inside_venv:
        print("Welcome to the construct")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)

        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.")
        packages: list[str] = site.getsitepackages()
        print("Package installation path:", packages[0] if packages else "Unknown")

    else:
        print("You're still plugged in")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: None detected")

        print(
            "\nWARNING: You're in the global environment!\n"
            "The machines can see everything you install."
        )
        print(
            "\nTo enter the construct, run:\n"
            "python3 -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
        )


if __name__ == '__main__':
    main()
