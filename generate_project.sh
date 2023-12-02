docker build \
        --build-arg UID=$(id -u) \
        --build-arg GID=$(id -g) \
        --force-rm \
        --tag cookiecutter-python-vscode \
        generator/ \
    && docker run --name cookiecutter-python-vscode \
        --user $(id -u) \
        --volume $(pwd):/work \
        --workdir /work \
        --interactive --tty \
        --rm \
        cookiecutter-python-vscode \
        bash /work/generator/run_cookiecutter.sh
