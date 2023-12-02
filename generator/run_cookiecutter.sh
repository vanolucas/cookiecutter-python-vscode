export PATH="$PATH:/home/cookiecutter/.local/bin" \
    && pip --disable-pip-version-check install --upgrade --user --no-cache-dir pipx \
    && pipx run cookiecutter .
