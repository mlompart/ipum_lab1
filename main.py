import os
import argparse
import sys
import yaml
from dotenv import load_dotenv
from settings import Settings


def load_dotenv_file(environment: str) -> None:
    """
    Loads environment variables from the specified .env file.
    """
    # Construct the path to the environment-specific .env file
    dotenv_path = f".env.{environment}"

    # Check if the specific .env file exists
    if not os.path.exists(dotenv_path):
        print(f"Error: Environment file '{dotenv_path}' not found.", file=sys.stderr)
        print(
            "Warning: Proceeding without loading from file. Relying on existing environment variables."
        )
        return

    print(f"Attempting to load environment variables from: {dotenv_path}")
    loaded = load_dotenv(dotenv_path=dotenv_path, override=True, verbose=True)

    if loaded:
        print(f"Successfully loaded environment variables from '{dotenv_path}'.")
    else:
        print(
            f"Warning: Could not load environment variables from '{dotenv_path}', although the file exists."
        )


def load_secrets_file(secrets_path: str = "secrets.yaml") -> None:
    """Loads secrets from a YAML file into environment variables."""

    secrets_file = "secrets.yaml"
    try:
        with open(secrets_file, "r") as f:
            secrets = yaml.safe_load(f)
            if secrets:  # Check if the file was not empty
                for key, value in secrets.items():
                    # Set environment variable, converting key to uppercase by convention
                    env_var_key = key.upper()
                    os.environ[key.upper()] = str(value)
                    print(f"Loaded secret: {env_var_key}")
            else:
                print(
                    f"Info: Secrets file '{secrets_path}' is empty or contains no data."
                )
    except FileNotFoundError:
        print(
            f"Warning: Secrets file not found at {secrets_file}. Make sure it's decrypted."
        )
    except yaml.YAMLError as e:  # Catch YAML parsing errors specifically
        print(f"Error parsing YAML secrets file {secrets_file}: {e}")
    except Exception as e:  # Catch other potential errors
        print(f"Error loading secrets from {secrets_file}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    # Call the two new functions separately
    load_dotenv_file(args.environment)
    load_secrets_file()  # Assumes secrets.yaml is in the current directory

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
