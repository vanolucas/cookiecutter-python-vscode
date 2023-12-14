from os import path
from shutil import copyfile

PROJECT_DIRECTORY = path.realpath(path.curdir)


if __name__ == "__main__":
    # Copy .env file from .devcontainer/ to root
    # Reason: newer docker-compose versions look for the .env file next to
    # the docker-compose.yml file
    root_env_path = path.join(PROJECT_DIRECTORY, ".env")
    devcontainer_env_path = path.join(PROJECT_DIRECTORY, ".devcontainer/.env")
    copyfile(devcontainer_env_path, root_env_path)
