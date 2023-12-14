# `{{ cookiecutter.project_name }}`

{{ cookiecutter.project_short_description }}

# Run dev environment

## Requirements

- VSCode with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- If on Linux:
  - `docker` and `docker-compose`
- If on Windows:
  - WSL2 and Docker Desktop

## Run VSCode dev container

First, open this folder in VSCode.

Then, reopen the project in a dev container by running one of these VSCode commands:
- `Dev Containers: Rebuild and Reopen in Container`: to build the dev container for the first time or rebuild it.
- `Dev Containers: Reopen in Container`: to open an existing container.

After the build, you may need to close then reopen the VSCode container for the Python code analysis tools to start up correctly.

# Run debug

Go to VSCode's `Run and Debug` tab to select what you want to launch. The listed configurations come from the [.vscode/launch.json](.vscode/launch.json) file.

`F5` runs the selected configuration.

# Run unit tests

In VSCode > `Testing` tab > `Refresh Tests`.

- Run all tests: `Test: Run All Tests`
- Debug all tests: `Test: Debug All Tests`
