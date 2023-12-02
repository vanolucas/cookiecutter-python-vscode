# List of supported image tags: https://mcr.microsoft.com/v2/devcontainers/python/tags/list
# `3.12` = Python 3.12 (released in October 2023)
# `bookworm` = Debian 12 (released in October 2023)
ARG IMAGE_VARIANT=3.12-bookworm

# Microsoft Python VSCode dev image: https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:${IMAGE_VARIANT}

# For real-time Python writes to stdout
ENV PYTHONUNBUFFERED 1

# Optional: install Debian packages
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Optional: if Python requirements rarely change, add them to the image
USER vscode
COPY requirements.txt /tmp/pip-tmp/
COPY .devcontainer/requirements.txt /tmp/pip-tmp/requirements-dev.txt
ENV PATH="${PATH}:/home/vscode/.local/bin"
RUN pip --disable-pip-version-check --no-cache-dir install --upgrade pip \
    && pip --no-cache-dir install --upgrade -r /tmp/pip-tmp/requirements.txt -r /tmp/pip-tmp/requirements-dev.txt
USER root
RUN rm -rf /tmp/pip-tmp
