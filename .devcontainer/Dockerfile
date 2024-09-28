FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Print the UID and GID
# CMD sh -c "echo 'Inside Container:' && echo 'User: $(whoami) UID: $(id -u) GID: $(id -g)'"

RUN apt update
RUN apt install -y zsh
RUN apt install -y fish
RUN apt install -y vim
RUN apt install -y neofetch
RUN apt install -y tesseract-ocr-eng

RUN pip install poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN echo 'alias ll="ls -lah --color=auto"' >> /home/vscode/.zshrc
RUN echo 'alias ll="ls -lah --color=auto"' >> /home/vscode/.zshrc

# RUN groupadd -g 1042 max
# RUN useradd -m -u 1042 -g -s /bin/fish max max
# RUN mkdir /app
# RUN chown max:max /app

# USER max
# WORKDIR /app

# RUN pip install poetry
# ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# RUN echo 'alias ll="ls -lah --color=auto"' >> /home/dev/.zshrc
# RUN echo 'alias ll="ls -lah --color=auto"' >> /home/dev/.zshrc
# RUN echo 'alias ll="ls -lah --color=auto"' >> /home/dev/.config/fish/config.fish


