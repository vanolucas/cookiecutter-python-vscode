# Cookiecutter template: Python VSCode project

A Cookiecutter template to generate VSCode dev container Python projects.

This also provides a Docker image to easily run the cookiecutter project generation tool.

# Usage

You can either generate a new project using the provided `./generate_project.sh` script or use `cookiecutter` directly.

## Using the provided Cookiecutter Docker image

To generate a new Python project, navigate to this folder, then:
```bash
./generate_project.sh
```

This will create then run a `cookiecutter-python-vscode` Docker image.

You will be prompted to provide a project name, etc.

The desired project folder gets created in the current directory.

Clean up after you generated your project with `generate_project.sh` (optional): you can delete the cookiecutter project generation Docker image with: `docker image rm cookiecutter-python-vscode`.

## Using Cookiecutter directly

Download directly from Github:
```bash
pipx run cookiecutter gh:vanolucas/cookiecutter-python-vscode
```

Or run in your local clone of this repo:
```bash
pipx run cookiecutter .
```
