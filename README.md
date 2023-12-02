# `cookiecutter-python-vscode`

Cookiecutter template for a sample VSCode dev container Python project.

This also provides a Docker image to easily run the cookiecutter project generation tool.

# Usage

To generate a new Python project, navigate to this folder, then:
```bash
./generate_project.sh
```

This will create then run a `cookiecutter-python-vscode` Docker image.

You will be prompted to provide a project name, etc.

The desired project folder gets created in the current directory.

# Clean up

You can delete the cookiecutter project generation Docker image with: `docker image rm cookiecutter-python-vscode`.
