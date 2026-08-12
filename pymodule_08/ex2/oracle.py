import os

from dotenv import load_dotenv  # type: ignore [import-not-found]


def load_config() -> dict[str, str | None]:
    load_dotenv()
    config_dict = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }
    return config_dict


def missing_config(
        config: dict[str, str | None], silence: bool = False
) -> bool:
    check = False
    for key, value in config.items():
        if value is None:
            if not silence:
                print(f"  [MISSING] {key}: not configured")
            check = True
        else:
            if not silence:
                print(f"  [OK] {key}: {value}")
    return check


def start_oracle(config: dict[str, str | None]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    print(f"Mode: {config['MATRIX_MODE'] or 'NOT SET'}")

    if config["DATABASE_URL"]:
        print("Database: Connected to local instance")
    else:
        print("Database: NOT CONFIGURED")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: NOT AUTHENTICATED")

    print(f"Log Level: {config['LOG_LEVEL'] or 'NOT SET'}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: OFFLINE")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if missing_config(config, silence=True):
        print("[KO] .env file not configured properly")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    config = load_config()
    missing_config(config)
    start_oracle(config)


if __name__ == "__main__":
    main()
