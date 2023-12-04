# List of supported image tags: https://mcr.microsoft.com/v2/devcontainers/python/tags/list
# `3.12` = Python 3.12 (released in October 2023)
# `bookworm` = Debian 12 (released in October 2023)
ARG IMAGE_VARIANT=3.12-bookworm

# Microsoft Python VSCode dev image: https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:${IMAGE_VARIANT}

# For real-time Python writes to stdout
ENV PYTHONUNBUFFERED 1

# Install pipx
USER vscode
ENV PATH="${PATH}:/home/vscode/.local/bin"
RUN pip --disable-pip-version-check --no-cache-dir install --upgrade pip \
    && pip --no-cache-dir install --user --upgrade \
    pipx
USER root
RUN rm -rf /tmp/pip-tmp

# Install Cookiecutter
USER vscode
RUN pipx install cookiecutter
USER root
