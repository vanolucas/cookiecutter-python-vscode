FROM python

ARG UID=1000
ARG GID=1000

RUN groupadd --gid ${GID} --non-unique cookiecutter
RUN useradd --uid ${UID} --gid ${GID} --create-home cookiecutter
