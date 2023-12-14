# `{{ cookiecutter.project_name }}`

{{ cookiecutter.project_short_description }}

# Requirements

- Docker and Docker Compose (also requires WSL2 on Windows)
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) VSCode extension

# Setup

A `.env` file must exist in this root directory and in `.devcontainer/`.
This file must contain all the environment variables needed to run the project locally.

[.env-sample](.env-sample) is a sample `.env` file.

# Run

First, open this folder in VSCode.

Then, reopen the project in a dev container by running one of these VSCode commands:
- `Dev Containers: Rebuild and Reopen in Container`: to build the dev container for the first time or rebuild it.
- `Dev Containers: Reopen in Container`: to open an existing container.

# Run debug

`F5` runs a configuration from the [.vscode/launch.json](.vscode/launch.json) file.

# Run unit tests

In VSCode > `Testing` tab > `Refresh Tests`.

- Run all tests: `Test: Run All Tests`
- Debug all tests: `Test: Debug All Tests`
