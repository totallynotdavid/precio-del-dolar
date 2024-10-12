# syntax=docker/dockerfile:1
ARG PYTHON_VERSION="3.12"
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION}

LABEL org.opencontainers.image.authors="David Duran <conctacto@altmails.com>"

RUN apt-get update && \
    apt-get full-upgrade -y && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER vscode

RUN mkdir -p ~/.local/bin

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Ensure Poetry binaries are in PATH for all subsequent commands
ENV PATH="/home/vscode/.local/bin:${PATH}"

# Enable Bash completions for Poetry
RUN poetry completions bash >> ~/.bash_completion && \
    echo 'source ~/.bash_completion' >> ~/.bashrc
