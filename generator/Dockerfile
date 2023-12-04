FROM python

ARG UID=1000
ARG GID=1000

# Create non-root user
RUN groupadd --gid ${GID} --non-unique cookiecutter
RUN useradd --uid ${UID} --gid ${GID} --create-home cookiecutter

# Install pipx
USER cookiecutter
ENV PATH="${PATH}:/home/cookiecutter/.local/bin"
RUN pip --disable-pip-version-check --no-cache-dir install --upgrade pip \
    && pip --no-cache-dir install --user --upgrade \
    pipx
USER root
RUN rm -rf /tmp/pip-tmp

# Install Cookiecutter
USER cookiecutter
RUN pipx install cookiecutter
USER root
